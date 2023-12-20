
//xyz

#include <Adafruit_TinyUSB.h>

#define LED LED_BUILTIN



void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);

  Serial1.setFIFOSize(1024);
  Serial1.begin(115200);
}


void loop() {
  digitalWrite(LED, true);
  delay(300);
  digitalWrite(LED, false);
  delay(300);
  Serial.println("Loopx");
  Serial1.println("Hardware serial");
}
