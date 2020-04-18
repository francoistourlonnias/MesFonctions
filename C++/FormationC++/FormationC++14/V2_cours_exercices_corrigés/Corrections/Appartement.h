#ifndef APPARTEMENT_H_INCLUDED
#define APPARTEMENT_H_INCLUDED

#include <iostream>
#include <memory>

#include "Canape.h"

class Appartement
{
    private :
    int m_nombrePieces, m_superficie;
    std::string m_couleurMur, m_typeSol;

    public :
    std::shared_ptr<Canape> m_canapSalon;


    Appartement(int nombrePieces, int superficie, std::string couleurMur, std::string typeSol, std::shared_ptr<Canape> canapSalon);
    ~Appartement();
    std::string description();
    void repeindre(std::string nouvelleCouleur);
    void remplacerCanape(int nombrePlaces, std::string motif, std::string couleur);

};

#endif // APPARTEMENT_H_INCLUDED
