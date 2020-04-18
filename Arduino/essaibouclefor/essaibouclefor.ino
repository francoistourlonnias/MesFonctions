// Eteint progressivement une LED en utilisant une broche PWM (impulsion)

int PWMpin = 10; // LED en série avec une résistance de 1k sur la broche 10
int nombre;
void setup()
{
      // Ouvre la voie série avec l'ordinateur
    Serial.begin(9600);
    Serial.println("port console initialise");
    // Ouvre la voie série avec le module BT
}

void loop()
{
   // boucle incrémentant la variable i de 0 à 255, de 1 en 1
/*   for (int i=0; i <= 50; i++){ 

Serial.print(i);Serial.print(" ... ");
nombre=random(0,7);
i=i+1;


   } // fin de la boucle for
   */
   nombre=random(0,7);
   Serial.println(nombre);
   Serial.println("fin de la boucle for");

   delay (1500);
}
