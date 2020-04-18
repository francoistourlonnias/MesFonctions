#ifndef DUREE_H_INCLUDED
#define DUREE_H_INCLUDED

    class Duree
    {

        private:

        int m_heures;
        int m_minutes;
        int m_secondes;

        public:

        Duree(int heures, int minutes, int secondes);
        void affichage();
        //On a besoin d'une méthode dans la classe
        //Pour accéder aux attributs
        bool estEgal(Duree duree2);
        Duree additionDurees(Duree d2);
        Duree soustractionDurees(Duree d2);

        //on modifie nos propres attribut donc il faut le mettre
        //dans la classe (deviens une méthode)
        void operator+=(Duree duree1);
        bool estInf(Duree duree2);

    };
    //La surcharge d'opérateur est hors de la classe
    bool operator==(Duree duree1, Duree duree2);
    Duree operator+(Duree duree1, Duree duree2);
    Duree operator-(Duree duree1, Duree duree2);
    bool operator<(Duree duree1, Duree duree2);


#endif // DUREE_H_INCLUDED
