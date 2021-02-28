#include <Arduino.h>
#include "TimerOne.h"

#define samplePeriod  0.02*1000*1000
#define wavePeriod 200

#define samplePin A0
#define wavePin 13

long int currentMillis = 0;
long int wavePrevMillis = 0;

bool waveState = LOW;

void handleSample() {
  Serial.println(analogRead(samplePin));
}

void setup() {

    // initialize LED digital pin as an output.
    Serial.begin(115200);
    pinMode(wavePin, OUTPUT);
    pinMode(samplePin, INPUT);

    Timer1.initialize(samplePeriod);
    Timer1.attachInterrupt(handleSample);

    delay(500);
   
}

void loop() {
    currentMillis = millis();

    if (currentMillis - wavePrevMillis >= wavePeriod) {
        wavePrevMillis = currentMillis;
        waveState = (waveState == LOW) ? HIGH : LOW;
        digitalWrite(wavePin, waveState);
    }
}
