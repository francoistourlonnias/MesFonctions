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
void ControlMotion();
double distance;
double AutorisationBouger;
double temporaire;
double R;
double V;
double B;
MeRGBLed rgbled_0(0, 12);
void Mouvement(double speed, String dir);
void compesLum();
double __var__108_117_109_105_110_111_115_105_116_233;
double compens;

void ControlMotion()
{
    if(((distance) < (8)) || (((distance)==(8)))){
        AutorisationBouger = 0;
        temporaire = R;
        R = 60;
    }else{
        AutorisationBouger = 1;
        R = temporaire;
        temporaire = 0;
    }
    V = V;
    B = B;
    rgbled_0.setColor(9,R,V,B);
    rgbled_0.show();
}

void Mouvement(double speed, String dir)
{
    ControlMotion();
    if(((dir)==(A))){
        if(((AutorisationBouger)==(1))){
            move(1,speed);
        }
    }
    if(((dir)==(R))){
        if(((AutorisationBouger)==(1))){
            move(2,speed);
        }
    }
    if(((dir)==(G))){
        if(((AutorisationBouger)==(1))){
            move(3,speed);
        }
    }
    if(((dir)==(D))){
        if(((AutorisationBouger)==(1))){
            move(4,speed);
        }
    }
    ControlMotion();
}

void compesLum()
{
    if((__var__108_117_109_105_110_111_115_105_116_233) < (50)){
        compens = ((-5.1) * (__var__108_117_109_105_110_111_115_105_116_233)) + (255);
        if((compens) > ( 255 )){
            compens = 255;
        }
        rgbled_0.setColor(0,compens,compens,compens);
        rgbled_0.show();
        compens = 60;
    }
}

void setup(){
    rgbled_0.setpin(44);
    attachInterrupt(Encoder_1.getIntNum(), isr_process_encoder1, RISING);
    attachInterrupt(Encoder_2.getIntNum(), isr_process_encoder2, RISING);
}

void loop(){
    _loop();
}

void _delay(float seconds){
    long endTime = millis() + seconds * 1000;
    while(millis() < endTime)_loop();
}

void _loop(){
    Encoder_1.loop();
    Encoder_2.loop();
}