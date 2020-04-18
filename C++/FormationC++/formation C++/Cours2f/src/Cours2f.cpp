//============================================================================
// Name        : Cours2f.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "Cours2f.hpp"
#include <iostream>

using namespace std;

Animal::Animal(string nom, string espece,int age) :
		m_nom(nom),m_espece(espece),m_age(age)
{
}
//surgcharge
Animal::Animal(string nom):
		m_nom(nom),m_espece("Inconnu"),m_age(0)
{
}
//Autre methode
void Animal::saluer()
{
	cout << "Bonjour ! je suis " << m_nom << endl;
	cout << "je suis un " << m_espece << " et jai ";
	cout << m_age << " ans.";
}

// getter - setter
int Animal::getAge()
{
	return m_age;
}

void Animal::setAge(int age)
{
	if (age >=0)
		m_age =age;
	else
		cout << "ERERRUR ! Age doit etre positif" << endl;
}

