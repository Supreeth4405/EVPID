#include <Arduino.h>
#include <Servo.h>
#include "Sensor.h"
#include "PID.h"

Servo servo;
Sensor sensor(10, 11);
PID pid(8.0, 0.625, 0.45, 15.0);

const int SERVO_MIN = 0;
const int SERVO_MAX = 130;
const int SERVO_CENTER = 65;

void setup()
{
  servo.attach(9);
  servo.write(SERVO_CENTER);

  Serial.begin(9600);

  sensor.begin();
  pid.begin();
}

void loop()
{
  float distance = sensor.getFilteredDistance();

  float output = pid.compute(distance);

  int servoAngle = SERVO_CENTER - output;

  servoAngle = constrain(servoAngle, SERVO_MIN, SERVO_MAX);

  servo.write(servoAngle);


  Serial.print(distance);
  Serial.print(",");

  Serial.print(pid.getError());
  Serial.print(",");

  Serial.print(servoAngle);
  Serial.print(",");

  Serial.println(millis()/1000.0);

  delay(75);
}