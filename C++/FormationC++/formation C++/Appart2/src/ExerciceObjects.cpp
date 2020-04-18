//============================================================================
// Name        : ExerciceObjects.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>

#include "ExerciceObjects.h"
using namespace std;


/*
Créez une classe Appartement avec comme variables de classe
deux int : m_nombrePieces et m_superficie
et deux String : m_couleurMur et m_typeSol.

Codez le constructeur de manière à ce qu'il initialise les attributs.

Développez la méthode description() qui retourne un string avec un petit texte
décrivant ces éléments. Faîtes en sorte que tous les éléments, attributs et méthodes
soient publics.
*/

//raw Appartement::Appartement(int nombrePieces,int superficie,string couleurMur, string typeSol,Canape* canapeSalon):
Appartement::Appartement(int nombrePieces,int superficie,string couleurMur, string typeSol,shared_ptr<Canape> canapeSalon):
	m_nombrePieces(nombrePieces),m_superficie(superficie),m_couleurMur(couleurMur),m_typeSol(typeSol),m_canapeSalon(canapeSalon)
		{
		}

std::string Appartement::description()
{
	std::string res= "Appartement compose de "+ to_string(m_nombrePieces) + "pieces "\
			+ " superficies " + to_string(m_superficie) \
			+ " couleur des murs " + m_couleurMur \
			+ " type de sol " + m_typeSol \
			+ " meuble d un " + m_canapeSalon->descriptionCanape();
	return res;
}


void Appartement::changer_sol()
{
	string nsol;
	cout << "entrer un type de sol";
	cin >> 	m_typeSol;
}

Canape::Canape(int nombrePlaces,string motif, string couleur):
		m_nombrePlaces(nombrePlaces), \
		m_motif(motif),m_couleur(couleur)
		{
		}

std::string Canape::descriptionCanape()
{
	std::string res= "Canape " \
			+ to_string(m_nombrePlaces) + " place(s) " \
			+ " avec " + m_motif + " de couleur " + m_couleur ;
	return res;
}
