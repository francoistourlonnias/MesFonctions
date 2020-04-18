/*
 * Heritages.h
 *
 *  Created on: 20 sept. 2016
 *      Author: ftourlon
 */

#ifndef HERITAGES_H_
#define HERITAGES_H_

class Felin
{
	//Attributs

	std::string m_nom;
	std::string m_espece;
	int m_age;

	public:
	//Constructeurs
	Felin(std::string nom,  std::string espece, int age);
	std::string seNourrir();
	std::string sePresenter();

};

class ChatSauvage : public Felin  //herite de Felin
{
	std::string m_proiePreferee;
public:
	ChatSauvage(std::string nom,  std::string espece, int age,std::string proiePreferee);
	//truc il faut rajouter les methodes surlequels on fait des surcharges!!!:
	std::string seNourrir();
	std::string sePresenter();
};

class ChatDomestique : public Felin  //herite de Felin
{
	std::string m_proiePreferee;
	std::string m_couleurCollier;
public:
	ChatDomestique(std::string nom,  std::string espece, int age,std::string proiePreferee,std::string couleurCollier);
	//truc il faut rajouter les methodes surlequels on fait des surcharges!!!:
	std::string seNourrir();
	std::string sePresenter();
};

#endif /* HERITAGES_H_ */
