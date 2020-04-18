/*
 * Couch.hpp
 *
 *  Created on: 18 juil. 2016
 *      Author: mmeinero
 */

#ifndef COUCH_HPP_
#define COUCH_HPP_
#include <string>

class Couch {
public:
	Couch();
	virtual ~Couch();
	Couch(int numberOfPlaces, std::string leather, std::string color);
	std::string description();
	void setColor(const std::string newColor);

private:
	int m_numberOfPlaces;
	std::string m_texture;
	std::string m_color;
};

#endif /* COUCH_HPP_ */
