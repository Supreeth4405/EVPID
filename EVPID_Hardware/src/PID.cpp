#include "PID.h"

PID::PID(float _Kp, float _Ki, float _Kd, float _setPoint)
{
    Kp = _Kp;
    ki = _Ki;
    kd = _Kd;
    setPoint = _setPoint;
}

void PID::begin()
{
    previousTime = millis();
    previousError = 0;
    integral = 0;
}

float PID::compute(float currentValue)
{
    unsigned long currentTime = millis();
    float dt = (currentTime - previousTime) / 1000.0;

    if (dt <= 0)
    {
        return 0;
    }
    previousTime = currentTime;

    float error = currentValue - setPoint;
    integral += error * dt;

    integral = constrain(integral, -50, 50);

    float derivative = (error - previousError) / dt;
    previousError = error;

    float output = (Kp * error) + (ki * integral) + (kd * derivative);
    return output;
}

float PID::getError()
{
    return previousError;
}