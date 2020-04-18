#ifndef APARTMENTEXCEPTION_H_
#define APARTMENTEXCEPTION_H_

#include <exception>
#include <string>

namespace std {

class AppartementException: public std::exception {
public:
	AppartementException(std::string errorMessage):
        m_errorMessage(errorMessage)
        {
        }
	virtual ~AppartementException()
	{
	}
	virtual const char* what() const throw(){
		return m_errorMessage.c_str();
	}
private:
	std::string m_errorMessage;
};

}

#endif
