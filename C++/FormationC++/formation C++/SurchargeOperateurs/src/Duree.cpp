
    #include "Duree.h"
    #include <iostream>

    using namespace std;

    Duree::Duree(int heures, int minutes, int secondes)
    : m_heures(heures), m_minutes(minutes), m_secondes(secondes)
    {
    }

    void Duree::affichage()
    {
 //   	cout << " appel methode affichage "<< endl;
        cout << "Duree de " << m_heures << "h ";
        cout << m_minutes << "min ";
        cout << m_secondes << "s" << endl;
    }

    //On écrit estEgal() dans la classe
    //pour utiliser les attributs
    bool Duree::estEgal(Duree duree2)
    {
        if(m_heures == duree2.m_heures &&
           m_minutes == duree2.m_minutes &&
           m_secondes == duree2.m_secondes)
            return true;
        else
            return false;
    }

    //On surcharge l'opérateur
    //Hors de la classe
    bool operator==(Duree duree1, Duree duree2)
    {
        if(duree1.estEgal(duree2))
            return true;
        else
            return false;
    }

    //On ecrit additionDurees dans la classe
    //pour utiliser les attributs
    Duree Duree::additionDurees(Duree d2)
    {

        int heures = m_heures+d2.m_heures;
        int minutes = m_minutes+d2.m_minutes;
        int secondes = m_secondes+d2.m_secondes;

        //On gère le cas où les minutes
        //ou les secondes depasseraient 60
        if(secondes >= 60)
        {
            secondes -= 60;
            minutes++;
        }

        if(minutes >= 60)
        {
            minutes -= 60;
            heures++;
        }

        return Duree(heures,minutes,secondes);
    }

    Duree Duree::soustractionDurees(Duree d2)
    {

        int heures = m_heures-d2.m_heures;
        int minutes = m_minutes-d2.m_minutes;
        int secondes = m_secondes-d2.m_secondes;

        //On gère le cas où les minutes
        //ou les secondes depasseraient 60
        if(secondes >= 60)
        {
            secondes -= 60;
            minutes++;
        }

        if(minutes >= 60)
        {
            minutes -= 60;
            heures++;
        }

        return Duree(heures,minutes,secondes);
    }
    //Surcharge de l'operateur hors de la classe
    Duree operator- (Duree duree1, Duree duree2)
    {
        return Duree(duree1.soustractionDurees(duree2));
    }

    //Surcharge de l'operateur hors de la classe
    Duree operator+ (Duree duree1, Duree duree2)
    {
        return Duree(duree1.additionDurees(duree2));
    }

    //difference fondamentale avec operator+ ici on ne retourne
    //pas une nouvelle valeur mais on enrichie l'entree...

    // le fait que l'on modifie nos propres attributs ce n'est plus une
    //fontcion mais une méthode
    void Duree::operator+=(Duree d2)
    {

         int heures = m_heures+d2.m_heures;
         int minutes = m_minutes+d2.m_minutes;
         int secondes = m_secondes+d2.m_secondes;
//cout << "debug heures" << heures << endl;
//cout << "debug minutes" << minutes << endl;
//cout << "debug secondes" << secondes << endl;
         //On gère le cas où les minutes
         //ou les secondes depasseraient 60
         if(secondes >= 60)
         {
             secondes -= 60;
             minutes++;
         }

         if(minutes >= 60)
         {
             minutes -= 60;
             heures++;
         }

         m_heures =  heures;
         m_minutes = minutes;
         m_secondes = secondes;
    }

    bool Duree::estInf(Duree duree2)
    {
    	//convertir en secondes
    	//car ici on tste deux a deux et si un des 3
    	//ne repond pas au test on donnera faux...
        if(m_heures < duree2.m_heures &&
           m_minutes < duree2.m_minutes &&
           m_secondes < duree2.m_secondes)
            return true;
        else
            return false;
    }

    //On surcharge l'opérateur
    //Hors de la classe
    bool operator<(Duree duree1, Duree duree2)
    {

        if(duree1.estInf(duree2))
            return true;
        else
            return false;
    }


