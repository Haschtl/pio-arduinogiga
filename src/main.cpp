#include <Arduino.h>
#include <Serial.h>
// #include <SerialRPC.h>
#define LED LED_BUILTIN

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  // SerialRPC.begin();
}
void loop() {
  digitalWrite(LED, digitalRead(LED) ^ 1); // toggle
  Serial.println("Test");
  // SerialRPC.println("Test");
  delay(1000);
}