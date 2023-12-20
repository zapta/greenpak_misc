#include <Adafruit_TinyUSB.h>
#include <Arduino.h>
#include <FreeRTOS.h>
#include <task.h>

#define LED

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  // USB serial.
  Serial.begin(115200);

  // Hardware serial.
  Serial1.setFIFOSize(1024);
  Serial1.begin(115200);
}

void loop() {
  digitalWrite(LED_BUILTIN, true);
  delay(300);
  digitalWrite(LED_BUILTIN, false);
  delay(300);
  Serial.println("Loop");
  Serial.flush();
  Serial1.println("Hardware serial");
}
