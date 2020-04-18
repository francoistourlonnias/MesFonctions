/*
 * ChatSauvage.h
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#ifndef CHATSAUVAGE_H_
#define CHATSAUVAGE_H_

#include <iostream>
#include "Felin.h"

class ChatSauvage : public Felin  //herite de Felin
{
	std::string m_proiePreferee;
public:
	ChatSauvage(std::string nom,  std::string espece, int age,std::string proiePreferee);
	//truc il faut rajouter les methodes surlequels on fait des surcharges!!!:
	std::string seNourrir();
	std::string sePresenter();
};


#endif /* CHATSAUVAGE_H_ */
