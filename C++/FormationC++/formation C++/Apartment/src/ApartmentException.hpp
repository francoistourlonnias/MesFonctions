/*
 * ApartmentException.hpp
 *
 *  Created on: 20 juil. 2016
 *      Author: mmeinero
 */

#ifndef APARTMENTEXCEPTION_HPP_
#define APARTMENTEXCEPTION_HPP_

#include <exception>
#include <string>

namespace std {

class ApartmentException: public exception {
public:
	ApartmentException(string errorMessage);
	virtual ~ApartmentException();
	virtual const char* what() const throw(){
		return m_errorMessage.c_str();
	}
private:
	string m_errorMessage;
};

} /* namespace std */

#endif /* APARTMENTEXCEPTION_HPP_ */
