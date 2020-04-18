#include <SoftwareSerial.h>
 
SoftwareSerial mySerial(7,8); // (RX, TX) (pin Rx BT, pin Tx BT)


void setup() {

 // Ouvre la voie série avec l'ordinateur
   Serial.begin(9600);
   while (!Serial) {
    ; //On attends que le port se connecte.
   }
   Serial.println(F("Arduino BT mode COMMUNICATION 9600."));
    // Ouvre la voie série avec le module BT
    mySerial.begin(9600);
       while (!mySerial) {
    ; //On attends que le port se connecte.
     }
  Serial.println(F("tout est pret"));
}

 
void loop() // run over and over
{
    if (mySerial.available()) {
       Serial.println(F("recu:"));
        Serial.write(mySerial.read());
    }
    if (Serial.available()) {
        Serial.println(F("envoi:"));
        mySerial.write(Serial.read());
    }
}
