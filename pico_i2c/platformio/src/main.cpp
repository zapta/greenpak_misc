#include <Adafruit_TinyUSB.h>
#include <Arduino.h>
#include <Wire.h>

// TODO: Add static asserts about the buffer size.
// TODO: Clear i2c available buffer before i2c read operation.

// NOTE: Arduino Wire API documentation is here
// https://www.arduino.cc/reference/en/language/functions/communication/wire/

// All command bytes must arrive within this time period.
// static constexpr uint32_t kCommandTimeoutMillis = 250;
static constexpr uint32_t kCommandTimeoutMillis = 0xffffffff;

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

static uint8_t i2c_write(uint8_t addr, uint8_t* bfr, uint8_t count) {
  Wire.beginTransmission(addr);
  Wire.write(bfr, count);
  const uint8_t status = Wire.endTransmission(true);
  return status;
}

// Abstract base of all command handlers.
class Command {
 public:
  Command(const char* name) : _name(name) {}
  const char* name() const { return _name; }
  // Called each time the command starts to allow initialization.
  virtual void enter() {}
  // Returns true if command completed.
  virtual bool loop() = 0;
  // Call if the command is aborted due to timeout.
  virtual void abort() {}

 private:
  const char* _name;
};

// // Handler for the do nothing command.
// static class NopCommand : public Command {
//  public:
//   NopCommand() : Command("nop") {}
//   virtual bool loop() { return true; }
// } nop_command;

// Handler for the 'echo' command which echoes the data byte.
static class EchoCommand : public Command {
 public:
  EchoCommand() : Command("echo") {}
  virtual bool loop() override {
    if (!read_input_bytes(data_buffer, 1)) {
      return false;
    }
    // digitalWrite(LED_BUILTIN, true);
    // for (;;) {
    // }

    // Serial.printf("[%02x]\n", data_buffer[0]);
    Serial.write(data_buffer[0]);
    return true;
  }
} echo_command;

// Handler for the 'start' command which sends the start byte of a read
// or write transaction.
static class WriteCommand : public Command {
 public:
  WriteCommand() : Command("write") {}
  virtual void enter() override { _got_cmd_header = false; }
  virtual bool loop() override {
    if (!_got_cmd_header) {
      // Read address byte and count byte.
      if (!read_input_bytes(data_buffer, 2)) {
        return false;
      }
      _got_cmd_header = true;
    }
    // Read (byte_count) bytes.
    if (!read_input_bytes(&data_buffer[2], data_buffer[2])) {
      return false;
    }
    const uint32_t status =
        i2c_write(data_buffer[0], &data_buffer[2], data_buffer[2]);
    Serial.write(status);
    return true;
  }

 private:
  bool _got_cmd_header = false;

} start_command;

// Handler for the 'read' command which reads N bytes.
static class ReadCommand : public Command {
 public:
  ReadCommand() : Command("read") {}

  virtual bool loop() override {
    // Get the address and the count bytes.
    if (!read_input_bytes(data_buffer, 2)) {
      return false;
    }
    const uint8_t addr = data_buffer[0] | 0x01;
    const uint8_t count = data_buffer[1];
    const size_t actual_count = Wire.requestFrom(addr, count, true);
    // Send error response.
    if (actual_count != count || Wire.available() != count) {
      Serial.write("F");
      return true;
    }
    // Send OK response with the data read
    Serial.write("P");
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

  // Hardware serial.
  Serial1.setFIFOSize(1024);
  Serial1.begin(115200);

  // Wire.setSDA(0);
  // Wire.setSCL(1);
  // Pins are SD=4, SCL=5
  Wire.setClock(100000);
  Wire.begin();
}

// If in command, points to the command handler.
static Command* current_cmd = nullptr;

void loop() {
  // Serial.printf("Loop %s\n", current_cmd? current_cmd->name() : "-");
  // delay(300);

  Serial.flush();
  const uint32_t millis_now = millis();
  const bool blink = current_cmd || (millis_now - last_command_start_millis) < 200;
  // millis_now & 0x0040 : millis_now & 0x0100;
  // const bool blink = current_cmd;
  digitalWrite(LED_BUILTIN, blink);

  // If a command is in progress, handle it.
  if (current_cmd) {
    const bool cmd_completed = current_cmd->loop();
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
