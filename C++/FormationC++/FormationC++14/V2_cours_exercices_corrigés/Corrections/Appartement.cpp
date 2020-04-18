#include <iostream>
#include "Appartement.h"
#include "Canape.h"
#include "AppartementException.h"

using namespace std;

Appartement::Appartement(int nombrePieces, int superficie, std::string couleurMur, std::string typeSol, shared_ptr<Canape> canapSalon) :
    m_nombrePieces(nombrePieces),m_superficie(superficie),m_couleurMur(couleurMur),m_typeSol(typeSol),m_canapSalon(canapSalon)
    {
        if (superficie < 9)
            throw AppartementException("Surface inferieure a 9m carres !");
    }

Appartement::~Appartement()
{
}

string Appartement::description()
{
    string s = "";
    s+= "Je suis un appartment " + to_string(m_nombrePieces) + " pieces de " + to_string(m_superficie) + "m2.\n";
    s+= "Mes murs sont " + m_couleurMur + "s et mon sol est en " + m_typeSol +"\n";
    s+= "Mon canape va se presenter lui meme : \n";
    s+= m_canapSalon->descriptionCanape();
    return s;
}

void Appartement::repeindre(string nouvelleCouleur)
{
    m_couleurMur = nouvelleCouleur;
}

void Appartement::remplacerCanape(int nombrePlaces, string motif, string couleur)
{
    shared_ptr<Canape> canap = make_shared<Canape>(nombrePlaces, motif, couleur);
    m_canapSalon = canap;
}
