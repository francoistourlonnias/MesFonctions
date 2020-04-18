/*
 * Couch.cpp
 *
 *  Created on: 18 juil. 2016
 *      Author: mmeinero
 */

#include "Couch.hpp"
#include <iostream>

using namespace std;

Couch::Couch() :
m_numberOfPlaces(5), m_texture("leather"), m_color("cream")
{
	// TODO Auto-generated constructor stub

}

Couch::~Couch() {
	// TODO Auto-generated destructor stub
}

Couch::Couch(int numberOfPlaces, std::string texture, std::string color):
m_numberOfPlaces(numberOfPlaces), m_texture(texture), m_color(color)
{

}

string Couch::description()
{
	string description("");

	description+="Couch description\n";
	description+="Number of places: " + std::to_string(m_numberOfPlaces) +"\n";
	description+="Texture: " + m_texture +"\n";
	description+="Color: " + m_color +"\n";
	description += "\n";

	return description;
}

void Couch::setColor(const std::string newColor)
{
	m_color = newColor;
}
