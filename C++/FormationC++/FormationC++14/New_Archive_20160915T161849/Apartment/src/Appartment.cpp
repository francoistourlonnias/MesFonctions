/*
 * Appartment.cpp
 *
 *  Created on: 18 juil. 2016
 *      Author: mmeinero
 */

#include <iostream>
#include <string>
#include "Apartment.hpp"
#include "ApartmentException.hpp"

using namespace std;

Apartment::Apartment() :
m_numberOfRooms(5), m_surface(120), m_walColor("white"), m_floorType("wooden"), m_livingRoomCouchPointer(NULL),m_diningRoomCouchPointer(NULL)
{

}

Apartment::Apartment(int surface):
m_numberOfRooms(5), m_surface(surface), m_walColor("white"), m_floorType("wooden"), m_livingRoomCouchPointer(NULL)
{
	if (9 > m_surface)
		throw ApartmentException("Apartment surface smaller than 9 sq meters");
}

Apartment::~Apartment() {

}

bool operator==(Apartment apartmentOne, Apartment apartmentTwo)
{
	if((apartmentOne.getSurface() == apartmentTwo.getSurface()) &&
			(apartmentOne.getWalColor() == apartmentTwo.getWalColor())&&
			(apartmentOne.getNumberOfRooms() == apartmentTwo.getNumberOfRooms())&&
			(apartmentOne.getFloorType() == apartmentTwo.getFloorType()))
		return true;
	else
		return false;
}

Apartment::Apartment(int numberOfPlaces, std::string texture, std::string color) :
m_numberOfRooms(5), m_surface(120), m_walColor("white"), m_floorType("wooden"), m_livingRoomCouchPointer(NULL),m_diningRoomCouchPointer(NULL)
{
	//m_diningRoomCouchPointer(new Couch(numberOfPlaces,texture,color));

	std::shared_ptr<Couch> pMyCouch(new Couch(numberOfPlaces,texture,color));
	m_diningRoomCouchPointer=pMyCouch;
}

Apartment::Apartment(Apartment const& apartmentToCopy):
m_numberOfRooms(apartmentToCopy.m_numberOfRooms),
m_surface(apartmentToCopy.m_surface),
m_walColor(apartmentToCopy.m_walColor),
m_floorType(apartmentToCopy.m_floorType),
m_livingRoomCouchPointer(NULL)
{
}

string Apartment::description()
{
	string description ("");
	description += "Apartment description \n";
	description += "Number of rooms: " + std::to_string(m_numberOfRooms) +"\n";
	description += "Surface (mq): " + std::to_string(m_surface) +"\n";
	description += "Wal color: " + m_walColor +"\n";
	description += "Flor type: " + m_floorType +"\n";
	if (NULL != m_livingRoomCouchPointer)
		description += m_livingRoomCouchPointer->description();
	if (NULL != m_diningRoomCouchPointer)
		description += m_diningRoomCouchPointer->description();
	description += "\n";

	return description;
}

void Apartment::paint(const string newColor)
{
	m_walColor=newColor;
}

void Apartment::setCouch(Couch* myCouchPointer)
{
	m_livingRoomCouchPointer = myCouchPointer;
}


