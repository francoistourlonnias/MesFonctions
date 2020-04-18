/*
 * Oiseau.hpp
 *
 *  Created on: 23 sept. 2016
 *      Author: ftourlon
 */

#ifndef OISEAU_HPP_
#define OISEAU_HPP_

#include "Cours2f.hpp"
#include <iostream>

using namespace std;

class Oiseau : public Animal
{
	std::string m_nid;

	public:
	Oiseau(std::string nom, std::string espece, int age, std::string nid);
	void saluer();
	void voler();
};


#endif /* OISEAU_HPP_ */
