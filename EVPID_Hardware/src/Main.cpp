#include <Arduino.h>
#include <Servo.h>
#include "Sensor.h"
#include "PID.h"

float Kp = 8;
float Ki = 0.625;
float Kd = 0.45;
float SetPoint = 15.0;

Servo servo;
Sensor sensor(10, 11);
PID pid(Kp, Ki, Kd, SetPoint);

const int SERVO_MIN = 0;
const int SERVO_MAX = 130;
const int SERVO_CENTER = 65;

bool PID_Control = false;

int servoAngle = SERVO_CENTER;
float output = 0;

void Update_New_Values();

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
  Update_New_Values();
  float distance = sensor.getFilteredDistance();

  if (PID_Control)
  {
    output = pid.compute(distance);
    servoAngle = SERVO_CENTER - output;
    servoAngle = constrain(servoAngle, SERVO_MIN, SERVO_MAX);
    servo.write(servoAngle);
  }

  Serial.print(distance);
  Serial.print(",");

  Serial.print(pid.getError());
  Serial.print(",");

  Serial.print(servoAngle);
  Serial.print(",");

  Serial.print(millis()/1000.0);
  Serial.print(",");

  Serial.print(pid.getP());
  Serial.print(",");

  Serial.print(pid.getI());
  Serial.print(",");

  Serial.print(pid.getD());
  Serial.print(",");

  Serial.print(output);
  Serial.print(",");

  Serial.print(pid.getkp());
  Serial.print(",");

  Serial.print(pid.getki());
  Serial.print(",");

  Serial.print(pid.getkd());
  Serial.print(",");

  Serial.println(pid.SetPoint());

  delay(50);
}

void Update_New_Values()
{
  if (Serial.available())
  {
    String msg = Serial.readStringUntil('\n');

    if (msg.startsWith("Kp:"))
    {
      Kp = msg.substring(3).toFloat();
      pid.Update_Kp(Kp);
    }

    if (msg.startsWith("Ki:"))
    {
      Ki = msg.substring(3).toFloat();
      pid.Update_Ki(Ki);
    }

    if (msg.startsWith("Kd:"))
    {
      Kd = msg.substring(3).toFloat();
      pid.Update_Kd(Kd);
    }

    if (msg.startsWith("SP:"))
    {
      SetPoint = msg.substring(3).toFloat();
      pid.Update_SP(SetPoint);
    }

    if (msg == "SERVO_OFF")
    {
      servo.detach();
    }
    else if (msg == "SERVO_ON")
    {
      servo.attach(9);
      servo.write(SERVO_CENTER);
    }

    if (msg == "PID_OFF")
    {
      PID_Control = false;
    }
    else if (msg == "PID_ON")
    {
      PID_Control = true;
    }
    
  }
}