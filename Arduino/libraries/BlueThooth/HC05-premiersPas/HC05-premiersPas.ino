 
#include <SoftwareSerial.h>
SoftwareSerial mavoieserie(11, 10); // (RX, TX) (pin Rx BT, pin Tx BT)
String  saisie = "";
int aenvoyer=0;
const int alim = 13;
const int key = 12;
String inString = "";    // string to hold input
void setup()
{

    // Ouvre la voie série avec l'ordinateur
    Serial.begin(9600);
    Serial.println("port console initialise");
    // Ouvre la voie série avec le module BT
    mavoieserie.begin(9600);
    Serial.println("port BT initialise");

    // partie pour pouvoir passer en mde AT (lorsque cette pin sera hight)
    // init de depart on sera en mode communication  
	//pinMode(alim, OUTPUT);
    //pinMode(alim, LOW); Serial.println("port EN LOW init");
    pinMode(key, OUTPUT);
    pinMode(key, LOW); Serial.println("port EN LOW init");
    Serial.println("port Commande initialise etat BAS (mode communication)");

    Serial.println("=== === FIN INITIALISATION === ===");
}

String extractSerial()
{
  String v=".u";
  // Read serial input:
  int inChar = Serial.read();
  // convert the incoming byte to a char
  // and add it to the string:
     inString += (char)inChar;

 // if you get a newline, print the string,
 // then the string's value:
    if (inChar == '\n') 
    {
      //Serial.println("Value:");
      v=inString;
      // clear the string for new input:
      inString = "";
    }
    //Serial.print("Debug0 ");    Serial.print(inChar);    Serial.println(v);
   return inChar,v;
}
void loop() // run over and over
{
	// ici on lit ce que le module BT envoie
    if (mavoieserie.available()) {
        Serial.write(mavoieserie.read());
    }
	// Si unecommande est envoyée sur la console Série Ordinateur
    if (Serial.available()) {
      //si le text commence par AT alors passer key a hight
      aenvoyer,saisie=extractSerial();
	  Serial.println("Debug detail console ordi ");       Serial.print(aenvoyer);      Serial.println(saisie);
      if (saisie.startsWith("AT",0) )
      {
        Serial.println("=== === COMMANDE AT === ===");
        pinMode(key, HIGH);Serial.println("port EN HIGH");
      }
      else
      {
        pinMode(key, LOW);Serial.println("port EN LOW");
      }
      Serial.print("==> ");Serial.print(saisie);
      int taille = sizeof(saisie);
      int bytesSent = mavoieserie.write(saisie,taille);
      Serial.println(bytesSent);
    }
}
