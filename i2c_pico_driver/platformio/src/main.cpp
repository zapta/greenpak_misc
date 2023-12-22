// #include <Adafruit_TinyUSB.h>
#include <Arduino.h>
#include <Wire.h>

// TODO: Add static asserts about the buffer size.
// TODO: Clear i2c available buffer before i2c read operation.
// TODO: Determine optimal led blinking policy.
// TODO: Investigate if we get a better resolution or failure errors.
// TODO: Add a RESET command.
// TODO: Add an INFO command, with version, etc.
// TODO: Add support for pullup control.

// NOTE: Arduino Wire API documentation is here
// https://www.arduino.cc/reference/en/language/functions/communication/wire/

// All command bytes must arrive within this time period.
static constexpr uint32_t kCommandTimeoutMillis = 250;
// static constexpr uint32_t kCommandTimeoutMillis = 0xffffffff;

static uint8_t data_buffer[500];

static uint32_t last_command_start_millis = 0;

// Read exactly n chanrs to data buffer. If not enough bytes, none is read
// and the function returns false.
static bool read_input_bytes(uint8_t* bfr, uint16_t n) {
  // Handle the case where not enough chars.
  const int avail = Serial.available();
  if (avail < (int)n) {
    return false;
  }

  // TODO: Verify actual read == n;
  size_t actual_read = Serial.readBytes(bfr, n);
  (void)actual_read;
  return true;
}

// Abstract base of all command handlers.
class CommandHandler {
 public:
  CommandHandler(const char* name) : _name(name) {}
  const char* cmd_name() const { return _name; }
  // Called each time the command starts to allow initialization.
  virtual void on_cmd_entered() {}
  // Returns true if command completed.
  virtual bool on_cmd_loop() = 0;
  // Call if the command is aborted due to timeout.
  virtual void on_cmd_aborted() {}

 private:
  const char* _name;
};

// ECHO command.
static class EchoCommandHandler : public CommandHandler {
 public:
  EchoCommandHandler() : CommandHandler("ECHO") {}
  virtual bool on_cmd_loop() override {
    if (!read_input_bytes(data_buffer, 1)) {
      return false;
    }
    Serial.write(data_buffer[0]);
    return true;
  }
} echo_cmd_handler;

// INFO command.
static class InfoCommandHandler : public CommandHandler {
 public:
  InfoCommandHandler() : CommandHandler("INFO") {}
  virtual bool on_cmd_loop() override {
    Serial.write(0x01);  // Number of bytes to follow.
    Serial.write(0x01);  // API version.
    return true;
  }
} info_cmd_handler;

// WRITE command.
//
// Returned status:
//  0 : Success
//  1 : Data too long
//  2 : NACK on transmit of address
//  3 : NACK on transmit of data
//  4 : Other error
//  5 : Timeout
static class WriteCommandHandler : public CommandHandler {
 public:
  WriteCommandHandler() : CommandHandler("WRITE") {}
  virtual void on_cmd_entered() override { _got_cmd_header = false; }
  virtual bool on_cmd_loop() override {
    // Read command header.
    if (!_got_cmd_header) {
      if (!read_input_bytes(data_buffer, 2)) {
        return false;
      }
      _got_cmd_header = true;
    }
    // Read command data bytes.
    const uint8_t count = data_buffer[1];
    if (!read_input_bytes(&data_buffer[2], count)) {
      return false;
    }
    // Device address is 7 bits LSB.
    const uint8_t device_addr = data_buffer[0];
    // Wire.clearTimeoutFlag();
    Wire.beginTransmission(device_addr);
    Wire.write(&data_buffer[2], count);
    const uint8_t status = Wire.endTransmission(true);

    // Return response.
    Serial.write(status ? 'E' : 'K');
    Serial.write(status);
    return true;
  }

 private:
  bool _got_cmd_header = false;

} write_cmd_handler;

// READ command.
static class ReadCommandHandler : public CommandHandler {
 public:
  ReadCommandHandler() : CommandHandler("READ") {}

  virtual bool on_cmd_loop() override {
    // Get the command address and the count.
    if (!read_input_bytes(data_buffer, 2)) {
      return false;
    }

    // Device address is 7 bits LSB.
    const uint8_t device_addr = data_buffer[0];
    const uint8_t count = data_buffer[1];
    // Wire.clearTimeoutFlag();
    const size_t actual_count = Wire.requestFrom(device_addr, count, true);
    // Send error response.
    // const bool had_timeout = Wire.getTimeoutFlag();
    uint8_t status = 0x00;
    if (actual_count != count) {
      status |= 0x01;
    }
    if (Wire.available() != count) {
      status |= 0x02;
    }
    if (status != 0) {
      Serial.write("E");
      Serial.write(status);
      return true;
    }
    // Here when OK, send status, count, and data.
    Serial.write("K");
    Serial.write(count);
    for (uint16_t i = 0; i < count; i++) {
      Serial.write(Wire.read());
    }
    return true;
  }

} read_cmd_handler;

// Given a command char, return a Command pointer or null if invalid command
// char.
static CommandHandler* find_command_handler_by_char(const char cmd_char) {
  switch (cmd_char) {
    case 'e':
      return &echo_cmd_handler;
    case 'i':
      return &info_cmd_handler;
    case 'w':
      return &write_cmd_handler;
    case 'r':
      return &read_cmd_handler;
    default:
      return nullptr;
  }
}

void setup() {
  // SerialUSB.begin(19200);
  pinMode(LED_BUILTIN, OUTPUT);

  // USB serial.
  // Per https://arduino-pico.readthedocs.io/en/latest/serial.html
  Serial.begin(115200);

  // Pins are SD=4, SCL=5
  Wire.setClock(100000);   // 100Khz.
  Wire.setTimeout(50000);  // 50ms timeout.
  Wire.begin();
}

// If in command, points to the command handler.
static CommandHandler* current_cmd = nullptr;

void loop() {
  // Serial.printf("Loop %s\n", current_cmd? current_cmd->name() : "-");
  // delay(300);

  Serial.flush();
  const uint32_t millis_now = millis();
  const bool blink =
      current_cmd || (millis_now - last_command_start_millis) < 200;
  // millis_now & 0x0040 : millis_now & 0x0100;
  // const bool blink = current_cmd;
  digitalWrite(LED_BUILTIN, blink);

  // If a command is in progress, handle it.
  if (current_cmd) {
    const bool cmd_completed = current_cmd->on_cmd_loop();
    if (cmd_completed) {
      current_cmd = nullptr;
    } else if (millis() - last_command_start_millis > kCommandTimeoutMillis) {
      current_cmd->on_cmd_aborted();
      current_cmd = nullptr;
    }
    return;
  }

  // Not in a command. Test if a char arrived to select the next command.
  if (!Serial.available()) {
    return;
  }

  // Dispatch the next command.
  const char cmd_char = Serial.read();
  current_cmd = find_command_handler_by_char(cmd_char);
  if (current_cmd) {
    last_command_start_millis = millis_now;
    current_cmd->on_cmd_entered();
  } else {
    // Unknown command selector. We ignore it silently.
  }
}
