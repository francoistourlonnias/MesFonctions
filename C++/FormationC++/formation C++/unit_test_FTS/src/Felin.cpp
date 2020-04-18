/*
 * Felin.cpp
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */


#include <iostream>
using namespace std;
#include "Felin.h"

//constructeur
Felin::Felin(std::string nom,  std::string espece, int age):
m_nom(nom),m_espece(espece),m_age(age)
{
}

//methode
std::string Felin::seNourrir()
{
	std::string res= " Je mange " ;
	return res;
}
std::string Felin::sePresenter()
{
	std::string res= " Je suis " + m_nom + " j ai "+ to_string(m_age) + " ans, je suis un " + m_espece ;
	return res;
}


