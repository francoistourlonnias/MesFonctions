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
	Créez une classe Appartement avec comme variables de classe
	deux int : m_nombrePieces et m_superficie
	et deux String : m_couleurMur et m_typeSol.

	Codez le constructeur de manière à ce qu'il initialise les attributs.

	Développez la méthode description() qui retourne un string avec un petit texte
	décrivant ces éléments. Faîtes en sorte que tous les éléments, attributs et méthodes
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
