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
Cr�ez une classe Appartement avec comme variables de classe
deux int : m_nombrePieces et m_superficie
et deux String : m_couleurMur et m_typeSol.

Codez le constructeur de mani�re � ce qu'il initialise les attributs.

D�veloppez la m�thode description() qui retourne un string avec un petit texte
d�crivant ces �l�ments. Fa�tes en sorte que tous les �l�ments, attributs et m�thodes
soient publics.
*/

std::string Appartement::description()
{
	std::string res= "nbre pieces "+ to_string(m_nombrePieces) + " superficies " + to_string(m_superficie) + " couleur des murs " + m_couleurMur+ " type de sol " + m_typeSol;
	return res;
}
Appartement::Appartement(int nombrePieces,int superficie,string couleurMur, string typeSol):
			m_nombrePieces(nombrePieces),m_superficie(superficie),m_couleurMur(couleurMur),m_typeSol(typeSol)
		{
		}

void Appartement::changer_sol()
{
	string nsol;
	cout << "entrer un type de sol";
	cin >> 	m_typeSol;
}


