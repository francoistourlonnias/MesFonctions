/*
 * Appartment.hpp
 *
 *  Created on: 18 juil. 2016
 *      Author: mmeinero
 */

#ifndef APARTMENT_HPP_
#define APARTMENT_HPP_

#include <iostream>
#include "Couch.hpp"
#include <memory>

class Apartment {
public:
	Apartment();
	virtual ~Apartment();
	Apartment(int surface);
	Apartment(Apartment const& apartmentToCopy);
	Apartment(int numberOfPlaces, std::string leather, std::string color);
	std::string description();
	void paint(const std::string newColor);
	void setCouch(Couch* myCouchPointer);
	int getSurface(){return m_surface;};
	int getNumberOfRooms(){return m_numberOfRooms;};
	std::string getWalColor(){return m_walColor;};
	std::string getFloorType(){return m_floorType;};

private:
	int m_numberOfRooms;
	int m_surface;
	std::string m_walColor;
	std::string m_floorType;
	Couch* m_livingRoomCouchPointer;
	std::shared_ptr<Couch> m_diningRoomCouchPointer;
};

bool operator ==(Apartment apartmentOne, Apartment apartmentTwo);

#endif /* APARTMENT_HPP_ */
