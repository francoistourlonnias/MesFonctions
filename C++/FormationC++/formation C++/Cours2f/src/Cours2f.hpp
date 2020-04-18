/*
 * Cours2f.hpp
 *
 *  Created on: 23 sept. 2016
 *      Author: ftourlon
 */

#ifndef COURS2F_HPP_
#define COURS2F_HPP_

#include <iostream>

class Animal
{
protected:
	//Attributs
	std::string m_nom;
	std::string m_espece;
	int m_age;

public:
	//constructeur
	Animal(std::string nom, std::string espece, int age);
	//surcharge
	Animal(std::string nom);

	//destructeur
	~Animal() { std::cout << "je passe dans le destructeur";}

	// getter - setter
	int getAge();
	void setAge(int);
	//Autre methode
	virtual void saluer();

};

#endif /* COURS2F_HPP_ */
