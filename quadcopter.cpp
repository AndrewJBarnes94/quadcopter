#include <iostream>
#include <string>
#include <map>

int MAXSPEED = 100;
int MINSPEED = 0;

int motor1 = 0;
int motor2 = 0;
int motor3 = 0;
int motor4 = 0;

int hover( int motor_speed ) {
    motor1 = motor_speed;
    motor2 = motor_speed;
    motor3 = motor_speed;
    motor4 = motor_speed;

    return motor_speed;
}

int main() {
    std::cout << hover(10);
}