
#include <SoftwareSerial.h>
const int key = 12; 
SoftwareSerial mavoieserie(11, 10); // (RX, TX) (pin Rx BT, pin Tx BT)
 
void setup()
{
    //iniialise la ligne key a bas au depart pour passer en mode AT
    pinMode(key, OUTPUT);
    pinMode(key, LOW);
    // Ouvre la voie série avec l'ordinateur
    Serial.begin(9600);
    // Ouvre la voie série avec le module BT
    mavoieserie.begin(9600);
}
 
void loop() // run over and over
{
    if (mavoieserie.available()) {
        Serial.write(mavoieserie.read());
    }
    if (Serial.available()) {
        mavoieserie.write(Serial.read());
    }
} 

