#include <SoftwareSerial.h>
#define LED_PIN 2

SoftwareSerial mySerial(8, 7); // RX, TX  
// Connect HM10      Arduino Uno
//     Pin 1/TXD          Pin 7
//     Pin 2/RXD          Pin 8

char inChar = 0;

void setup()  
{
  Serial.begin(9600);
  Serial.println("Device ready");
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  Serial.println("BT ready");

}

void loop() // run over and over
{
  if (mySerial.available()){
    inChar = mySerial.read();
    //Serial.println("recu ");
    Serial.write(inChar);
    delay(20);
    }
    
  if (Serial.available()>0){
    //Serial.println("envoye");
    mySerial.write(Serial.read());
  }
}
