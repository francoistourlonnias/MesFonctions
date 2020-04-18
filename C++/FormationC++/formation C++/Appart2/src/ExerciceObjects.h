/*
 * ExerciceObjects.h
 *
 *  Created on: 19 sept. 2016
 *      Author: ftourlon
 */

#ifndef EXERCICEOBJECTS_H_
#define EXERCICEOBJECTS_H_

#include <IOSTREAM>
#include <memory>  // pour les shared_ptr
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
	//raw Canape* m_canapeSalon;
	std::shared_ptr<Canape> m_canapeSalon;

	public:

	//Constructeurs
	//raw Appartement(int nombrePieces,int superficie,std::string couleurMur, std::string typeSol,Canape* canapeSalon);
	Appartement(int nombrePieces,int superficie,std::string couleurMur, std::string typeSol,std::shared_ptr<Canape> canapeSalon);

	std::string description();

	//methode public pour setter une valeur
	void changer_sol();

};



#endif /* EXERCICEOBJECTS_H_ */
