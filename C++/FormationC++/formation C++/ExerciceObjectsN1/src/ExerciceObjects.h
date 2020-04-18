/*
 * ExerciceObjects.h
 *
 *  Created on: 19 sept. 2016
 *      Author: ftourlon
 */

#ifndef EXERCICEOBJECTS_H_
#define EXERCICEOBJECTS_H_

#include <IOSTREAM>

class Appartement
{

	/*
	Cr�ez une classe Appartement avec comme variables de classe
	deux int : m_nombrePieces et m_superficie
	et deux String : m_couleurMur et m_typeSol.

	Codez le constructeur de mani�re � ce qu'il initialise les attributs.

	D�veloppez la m�thode description() qui retourne un string avec un petit texte
	d�crivant ces �l�ments. Fa�tes en sorte que tous les �l�ments, attributs et m�thodes
	soient publics.
	*/

	//Attributs
	int m_nombrePieces;
	int m_superficie;
	std::string m_couleurMur;
	std::string m_typeSol ;

	public:

	//Constructeurs
	Appartement(int nombrePieces,int superficie,std::string couleurMur, std::string typeSol);
	std::string description();

	//methode public pour setter une valeur
	void changer_sol();

};

class Canape
{
	//Attributs
	int m_nombrePlaces;
	std::string m_motif;
	std::string m_couleur;

	public:
	//Constructeurs  ATTENTION FAUX   PAS DE m_ ci dessous a voir!!!!
	Canape(int nombrePlaces,std::string m_motif,  std::string m_couleur );
	std::string descriptionCanape();

};

#endif /* EXERCICEOBJECTS_H_ */
