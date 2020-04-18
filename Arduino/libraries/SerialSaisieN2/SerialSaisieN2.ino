int affichageFait;// déclaration de la variable
String inString = "";    // string to hold input
void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  affichageFait=0;//initialisation de la variable
}

void affichageInit()
{
     
        //ce code n'est exécuté que si la condition est vérifiée
        Serial.println("Hello");
        Serial.println("Arduino");
        Serial.println("World !");
        affichageFait=1;//on passe la variable à 1 pour ne plus exécuter le code
    
}

int extractIntSerial()
{
  int v=0;
  // Read serial input:

    //Serial.print("Debug1 ");
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') 
    {
      //Serial.println("Value:");
      v=inString.toInt();
      /*Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);*/
      // clear the string for new input:
      inString = "";
    }
   
   return v;
}
void action(int t)
{
   // DEBUG Serial.print("entree case :"); Serial.println(t);
   switch (t) {
          case 10:    // your hand is on the sensor
            Serial.println(">>>>>>>>>>>>>>>>>>>>> 10");
            break;
          case 11:    // your hand is close to the sensor
            Serial.println(">>>>>>>>>>>>>>>>>>>>> 11");
            break;
          case 20:    // your hand is a few inches from the sensor
            Serial.println(">>>>>>>>>>>>>>>>>>>>> 20");
            break;
          case 21:    // your hand is nowhere near the sensor
            Serial.println(">>>>>>>>>>>>>>>>>>>>> 21");
            break;
        }
}
void loop()
{
  int v=0;
  if (affichageFait==0)
   {
     affichageInit();
   }
  while (Serial.available() > 0) 
   {
      v=extractIntSerial();
      //DEBUG Serial.print("entree action :"); Serial.println(v);
      action(v);
      delay(1);        // delay in between reads for stability
    }
  
}