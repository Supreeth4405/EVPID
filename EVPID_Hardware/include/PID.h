#ifndef pid_h
#define pid_h

#include <Arduino.h>

class PID
{
    private:
        float Kp, Ki, Kd;
        float P, I, D;
        float setPoint;
        float previousError;
        float integral;
        unsigned long previousTime = 0;
    public:
        PID(float Kp, float Ki, float Kd, float setPoint);
        void begin();
        float compute(float currentValue);
        float getError();
        float getP();
        float getI();
        float getD();
        float getkp();
        float getki();
        float getkd();
        float SetPoint();
        void Update_Kp(float Kp);
        void Update_Ki(float Ki);
        void Update_Kd(float Kd);
        void Update_SP(float SetPoint);
};

#endif