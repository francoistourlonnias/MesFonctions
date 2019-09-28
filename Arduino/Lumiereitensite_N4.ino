#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>

//Encoder Motor
MeEncoderOnBoard Encoder_1(SLOT1);
MeEncoderOnBoard Encoder_2(SLOT2);

void isr_process_encoder1(void)
{
      if(digitalRead(Encoder_1.getPortB()) == 0){
            Encoder_1.pulsePosMinus();
      }else{
            Encoder_1.pulsePosPlus();
      }
}

void isr_process_encoder2(void)
{
      if(digitalRead(Encoder_2.getPortB()) == 0){
            Encoder_2.pulsePosMinus();
      }else{
            Encoder_2.pulsePosPlus();
      }
}

void move(int direction, int speed)
{
      int leftSpeed = 0;
      int rightSpeed = 0;
      if(direction == 1){
            leftSpeed = -speed;
            rightSpeed = speed;
      }else if(direction == 2){
            leftSpeed = speed;
            rightSpeed = -speed;
      }else if(direction == 3){
            leftSpeed = -speed;
            rightSpeed = -speed;
      }else if(direction == 4){
            leftSpeed = speed;
            rightSpeed = speed;
      }
      Encoder_1.setTarPWM(leftSpeed);
      Encoder_2.setTarPWM(rightSpeed);
}
void moveDegrees(int direction,long degrees, int speed_temp)
{
      speed_temp = abs(speed_temp);
      if(direction == 1)
      {
            Encoder_1.move(-degrees,(float)speed_temp);
            Encoder_2.move(degrees,(float)speed_temp);
      }
      else if(direction == 2)
      {
            Encoder_1.move(degrees,(float)speed_temp);
            Encoder_2.move(-degrees,(float)speed_temp);
      }
      else if(direction == 3)
      {
            Encoder_1.move(-degrees,(float)speed_temp);
            Encoder_2.move(-degrees,(float)speed_temp);
      }
      else if(direction == 4)
      {
            Encoder_1.move(degrees,(float)speed_temp);
            Encoder_2.move(degrees,(float)speed_temp);
      }
}

double angle_rad = PI/180.0;
double angle_deg = 180.0/PI;
void LedDef(double led, String RVB, double Pas);
double cpt;
double __var__105_110_116_101_110_115_105_116_233;
double Pas;
MeRGBLed rgbled_0(0, 12);

void LedDef(double led, String RVB, double Pas)
{
    cpt = 0;
    __var__105_110_116_101_110_115_105_116_233 = 0;
    Pas = null;
    for(int __i__=0;__i__<509;++__i__)
    {
        if(((RVB)==(R))){
            cpt += (1) + (Pas);
            if((cpt) < (255)){
                __var__105_110_116_101_110_115_105_116_233 += (1) + (Pas);
                rgbled_0.setColor(led,__var__105_110_116_101_110_115_105_116_233,0,0);
                rgbled_0.show();
            }else{
                if((((cpt) > (255)) || (((cpt)==(255)))) && ((cpt) < (509))){
                    __var__105_110_116_101_110_115_105_116_233 += (-1) * (Pas);
                    rgbled_0.setColor(led,__var__105_110_116_101_110_115_105_116_233,0,0);
                    rgbled_0.show();
                }else{
                    cpt = 0;
                    __var__105_110_116_101_110_115_105_116_233 = 0;
                }
            }
        }
        if(((RVB)==(V))){
            cpt += (1) + (Pas);
            if((cpt) < (255)){
                __var__105_110_116_101_110_115_105_116_233 += (1) + (Pas);
                rgbled_0.setColor(led,0,__var__105_110_116_101_110_115_105_116_233,0);
                rgbled_0.show();
            }else{
                if((((cpt) > (255)) || (((cpt)==(255)))) && ((cpt) < (509))){
                    __var__105_110_116_101_110_115_105_116_233 += (-1) * (Pas);
                    rgbled_0.setColor(led,0,__var__105_110_116_101_110_115_105_116_233,0);
                    rgbled_0.show();
                }else{
                    cpt = 0;
                    __var__105_110_116_101_110_115_105_116_233 = 0;
                }
            }
        }
        if(((RVB)==(B))){
            cpt += (1) + (Pas);
            if((cpt) < (255)){
                __var__105_110_116_101_110_115_105_116_233 += (1) + (Pas);
                rgbled_0.setColor(led,0,0,__var__105_110_116_101_110_115_105_116_233);
                rgbled_0.show();
            }else{
                if((((cpt) > (255)) || (((cpt)==(255)))) && ((cpt) < (509))){
                    __var__105_110_116_101_110_115_105_116_233 += (-1) * (Pas);
                    rgbled_0.setColor(led,0,0,__var__105_110_116_101_110_115_105_116_233);
                    rgbled_0.show();
                }else{
                    cpt = 0;
                    __var__105_110_116_101_110_115_105_116_233 = 0;
                }
            }
        }
    }
}

void setup(){
    rgbled_0.setpin(44);
}

void loop(){
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
}
