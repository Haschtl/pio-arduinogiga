#include <Arduino.h>
#include <SerialRPC.h>
#define LED LED_BLUE

void setup() {
  pinMode(LED, OUTPUT);
  SerialRPC.begin();
}
void loop() {
  digitalWrite(LED, digitalRead(LED) ^ 1); // toggle
  SerialRPC.println("Test");
  delay(1000);
}