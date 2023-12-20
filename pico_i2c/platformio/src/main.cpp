#include <Adafruit_TinyUSB.h>
#include <Arduino.h>
#include <Wire.h>

// TODO: Add static asserts about the buffer size.
// TODO: Clear i2c available buffer before i2c read operation.

// NOTE: Arduino Wire API documentation is here
// https://www.arduino.cc/reference/en/language/functions/communication/wire/

// All command bytes must arrive within this time period.
static constexpr uint32_t kCommandTimeoutMillis = 250;
// static constexpr uint32_t kCommandTimeoutMillis = 0xffffffff;

static uint8_t data_buffer[500];

static uint32_t last_command_start_millis = 0;

// Read exactly n chanrs to data buffer. If not enough bytes, none is read
// and the function returns false.
static bool read_input_bytes(uint8_t* bfr, uint32_t n) {
  // Handle the case where not enough chars.
  const int avail = Serial.available();
  if (avail < n) {
    return false;
  }

  // We assume that exactly n bytes were read.
  size_t actual_read = Serial.read(bfr, n);
  return true;
}

static void clear_input() {
  while (Serial.available() > 0) {
    Serial.read();
  }
}

// Abstract base of all command handlers.
class Command {
 public:
  Command(const char* name) : _name(name) {}
  const char* name() const { return _name; }
  // Called each time the command starts to allow initialization.
  virtual void enter() {}
  // Returns true if command completed.
  virtual bool cmd_loop() = 0;
  // Call if the command is aborted due to timeout.
  virtual void abort() {}

 private:
  const char* _name;
};

// ECHO command.
static class EchoCommand : public Command {
 public:
  EchoCommand() : Command("echo") {}
  virtual bool cmd_loop() override {
    if (!read_input_bytes(data_buffer, 1)) {
      return false;
    }
    Serial.write(data_buffer[0]);
    return true;
  }
} echo_command;


// WRITE command.
//
// Returned status:
//  0 : Success
//  1 : Data too long
//  2 : NACK on transmit of address
//  3 : NACK on transmit of data
//  4 : Other error
//  5 : Timeout
static class WriteCommand : public Command {
 public:
  WriteCommand() : Command("write") {}
  virtual void enter() override { _got_cmd_header = false; }
  virtual bool cmd_loop() override {
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
    // I2C write to device.
    const uint8_t write_addr = data_buffer[0] & ~0x01;
    Wire.clearTimeoutFlag();
    Wire.beginTransmission(write_addr);
    Wire.write(&data_buffer[2], count);
    const uint8_t status = Wire.endTransmission(true);

    // Return response.
    Serial.write(status ? 'E' : 'K');
    Serial.write(status);
    return true;
  }

 private:
  bool _got_cmd_header = false;

} start_command;

// READ command.
static class ReadCommand : public Command {
 public:
  ReadCommand() : Command("read") {}

  virtual bool cmd_loop() override {
    // Get the command address and the count.
    if (!read_input_bytes(data_buffer, 2)) {
      return false;
    }
    const uint8_t read_addr = data_buffer[0] | 0x01;
    const uint8_t count = data_buffer[1];
    Wire.clearTimeoutFlag();
    const size_t actual_count = Wire.requestFrom(read_addr, count, true);
    // Send error response.
    const bool had_timeout = Wire.getTimeoutFlag();
    uint8_t status = 0x00;
    if (actual_count != count) {
      status |= 0x01;
    }
    if (Wire.available() != count) {
      status != 0x02;
    }
    if (Wire.getTimeoutFlag()) {
      status != 4;
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

} read_command;

// Given a command char, return a Command pointer or null if invalid command
// char.
static Command* find_command_by_char(const char cmd_char) {
  switch (cmd_char) {
    case 'e':
      return &echo_command;
    case 'w':
      return &start_command;
    case 'r':
      return &read_command;
    default:
      return nullptr;
  }
}

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  // USB serial.
  Serial.begin(115200);

  // Pins are SD=4, SCL=5
  Wire.setClock(100000);         // 100Khz.
  Wire.setTimeout(50000, true);  // 50ms timeout. Reset on timeout.
  Wire.begin();
}

// If in command, points to the command handler.
static Command* current_cmd = nullptr;

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
    const bool cmd_completed = current_cmd->cmd_loop();
    if (cmd_completed) {
      // Serial.println("Completed");
      current_cmd = nullptr;
    } else if (millis() - last_command_start_millis > kCommandTimeoutMillis) {
      // Serial.println("Cmd timeout");
      current_cmd->abort();
      current_cmd = nullptr;
    }
    return;
  }

  // Not in a command. If a command char arrived, dispatch the command.
  if (!Serial.available()) {
    return;
  }

  const char cmd_char = Serial.read();
  current_cmd = find_command_by_char(cmd_char);
  // Enter the command or ignore the unknown char silently.
  if (current_cmd) {
    last_command_start_millis = millis_now;
    current_cmd->enter();
  }
}
