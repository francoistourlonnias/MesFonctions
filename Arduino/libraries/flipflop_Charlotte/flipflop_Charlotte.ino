
const int CNXLED13=13;
const int CNXLED2=2;
int tempsDePause;
char etat;
char etat2;


void setup()

{

  pinMode(CNXLED13,OUTPUT); // 0 volt
  pinMode(CNXLED2,OUTPUT);  // 5 volts
  tempsDePause=1000;
  etat= HIGH;
  etat2= LOW;
}


void loop()

{

if (etat == HIGH)
{ etat = LOW;
  etat2= HIGH;}
else
{ etat = HIGH;
  etat2= LOW;}

  digitalWrite(CNXLED13,etat);
  digitalWrite(CNXLED2,etat2);
  delay(tempsDePause);

}
