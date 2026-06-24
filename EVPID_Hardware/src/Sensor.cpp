#include "Sensor.h"


Sensor::Sensor(int trig, int echo)
{
  trigPin = trig;
  echoPin = echo;
}


void Sensor::begin()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}


long Sensor::getDistance()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, Timeout);

  return duration * 0.0343 / 2;
}


float Sensor::getFilteredDistance()
{
  float sum = 0;

  for (int i = 0; i < 3; i++)
  {
    sum += getDistance();
    delay(5);
  }

  return sum / 3.0;
}