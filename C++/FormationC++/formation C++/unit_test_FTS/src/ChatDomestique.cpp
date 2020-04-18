/*
 * ChatDomestique.cpp
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#include <iostream>
using namespace std;
#include "ChatDomestique.h"

ChatDomestique::ChatDomestique(std::string nom,  std::string espece, int age,std::string proiePreferee,std::string couleurCollier ):
Felin(nom,espece,age),m_proiePreferee(proiePreferee),m_couleurCollier(couleurCollier)
{
}
//methode
std::string ChatDomestique::seNourrir()
{
	std::string res= Felin::seNourrir() + m_proiePreferee ;
	return res;
}
std::string ChatDomestique::sePresenter()
{
	std::string res= Felin::sePresenter() +"la couleur de mon collier est " + m_couleurCollier;
	return res;
}

