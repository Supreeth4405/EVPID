#ifndef pid_h
#define pid_h

#include <Arduino.h>

class PID
{
    private:
        float Kp, ki, kd;
        float setPoint;
        float previousError;
        float integral;
        unsigned long previousTime = 0;
    public:
        PID(float Kp, float Ki, float Kd, float setPoint);
        void begin();
        float compute(float currentValue);
        float getError();
    
};

#endif