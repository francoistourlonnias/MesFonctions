
const int CNXLED13=13;
const int CNXLED7=7;
int tempsDePause;
char etat;
char etat7;


void setup()

{

  pinMode(CNXLED13,OUTPUT);
  pinMode(CNXLED7,OUTPUT);
  tempsDePause=1000;
  etat= HIGH;
  etat7= LOW;
}


void loop()

{

if (etat == HIGH)
{ etat = LOW;
  etat7= HIGH;}
else
{ etat = HIGH;
  etat7= LOW;}

  digitalWrite(CNXLED13,etat);
  digitalWrite(CNXLED7,etat7);
  delay(tempsDePause);

}
