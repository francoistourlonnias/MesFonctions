#ifndef CANAPE_H_INCLUDED
#define CANAPE_H_INCLUDED

#include <iostream>
#include <memory>

class Canape
{
    public :
    int m_nombrePlaces;
    std::string m_motif, m_couleur;


    public :
    Canape(int nombrePlaces, std::string motif, std::string couleur);
    std::string descriptionCanape();
    void changerMotif(std::string nouveauMotif);

};


#endif // CANAPE_H_INCLUDED
