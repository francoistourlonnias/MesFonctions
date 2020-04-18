/*
 * Oiseau.cpp
 *
 *  Created on: 23 sept. 2016
 *      Author: ftourlon
 */

#include "Cours2f.hpp"
#include "Oiseau.hpp"
#include <iostream>

using namespace std;

Oiseau::Oiseau (string nom, string espece, int age, string nid):
	Animal(nom,espece,age),m_nid(nid)
{
}
void Oiseau::saluer()
{
	Animal::saluer();
	cout << "Mon Nid s'appelle "  << m_nid << endl;

}
void Oiseau::voler()
{
	cout << endl <<"je vole !";
}
