/*
 * ChatSauvage.cpp
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#include <iostream>
using namespace std;
#include "ChatSauvage.h"

ChatSauvage::ChatSauvage(std::string nom,  std::string espece, int age,std::string proiePreferee ):
Felin(nom,espece,age),m_proiePreferee(proiePreferee)
{
}
//methode


std::string ChatSauvage::seNourrir()
{
	std::string res= Felin::seNourrir() + m_proiePreferee ;
	return res;
}
std::string ChatSauvage::sePresenter()
{
	std::string res= Felin::sePresenter() +"ma proie preferee est" + m_proiePreferee;
	return res;
}


