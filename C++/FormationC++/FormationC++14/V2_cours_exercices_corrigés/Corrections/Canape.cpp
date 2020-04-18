#include <iostream>
#include "Canape.h"

using namespace std;

Canape::Canape(int nombrePlaces, std::string motif, std::string couleur) :
    m_nombrePlaces(nombrePlaces),m_motif(motif),m_couleur(couleur)
    {
    }

string Canape::descriptionCanape()
{
    string s = "";
    s += "Je suis un canape " + to_string(m_nombrePlaces) + " places.\n";
    s += "Je suis " + m_couleur + " motif " + m_motif + "\n";
    return s;
}

void Canape::changerMotif(string nouveauMotif)
{
    m_motif = nouveauMotif;
}

