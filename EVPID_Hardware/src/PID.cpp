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

    P = (Kp * error);
    I = (ki * integral);
    D = (kd * derivative);

    float output = P + I + D;
    return output;
}

float PID::getError()
{
    return previousError;
}

float PID::getP()
{
    return P;
}

float PID::getI()
{
    return I;
}

float PID::getD()
{
    return D;
}

float PID::getkp()
{
    return Kp;
}

float PID::getki()
{
    return ki;
}

float PID::getkd()
{
    return kd;
}

float PID::SetPoint()
{
    return setPoint;
}