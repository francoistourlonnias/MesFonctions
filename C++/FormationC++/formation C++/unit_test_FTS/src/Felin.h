/*
 * Felin.h
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#ifndef FELIN_H_
#define FELIN_H_

#include <iostream>

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



#endif /* FELIN_H_ */
