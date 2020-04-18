/*
 * Duree.cpp
 *
 *  Created on: 20 juil. 2016
 *      Author: mmeinero
 */

#include "Duree.hpp"
#include <iostream>

using namespace std;

Duree operator-(const Duree & duree1, const Duree & duree2)
{
  int difference = duree1.dureeToSeconds() - duree2.dureeToSeconds();
  if (difference < 0)
    {
      return Duree(0,0,0);
    }
  return secondsToDuree(difference);
}

bool operator<(const Duree & duree1, const Duree & duree2)
{
  int difference = duree1.dureeToSeconds() - duree2.dureeToSeconds();
  if (difference < 0)
    {
      return true;
    }
  return false;
}

int Duree::dureeToSeconds() const
{
  return m_heure*3600+m_minute*60+m_seconde;
}

Duree secondsToDuree(const int p_seconds)
{
  int seconds = p_seconds % 60;
  int minutes = (p_seconds /60)%60;
  int heures = p_seconds / 3600;
  return Duree(heures, minutes, seconds);
}

string Duree::affiche()
{
  string message("");
  message+="Duree " + to_string(m_heure) + " h " + to_string(m_minute) + " \' " + to_string(m_seconde) + " \" " +  "\n";

  return message;
}

Duree Duree::operator+=(const Duree & p_duree)
{
  int somme = this->dureeToSeconds()+p_duree.dureeToSeconds();
  *this = secondsToDuree(somme);
  this->affiche();
  return *this;
}


