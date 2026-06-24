#ifndef sensor_h
#define sensor_h

#include <Arduino.h>

class Sensor
{
    private:
        int trigPin;
        int echoPin;
        const unsigned long Timeout = 30000;
    public:
        Sensor(int trig, int echo);
        void begin();
        long getDistance();
        float getFilteredDistance();
};

#endif