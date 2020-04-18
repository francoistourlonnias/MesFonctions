/*
 * ChatDomestique.h
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#ifndef CHATDOMESTIQUE_H_
#define CHATDOMESTIQUE_H_

#include <iostream>
#include "Felin.h"

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



#endif /* CHATDOMESTIQUE_H_ */
