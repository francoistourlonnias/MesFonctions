#ifndef FAUVE_H_INCLUDED
#define FAUVE_H_INCLUDED

#include "Felin.h"
#include <string>

class Fauve: public Felin {
public:
	Fauve(std::string nom, std::string espece, int age, std::string proiePreferee);
	virtual ~Fauve();
	std::string seNourrir();
    std::string seNourrir(std::string proieDuJour);
	std::string sePresenter();
private:
	std::string m_proiePreferee;
};


#endif // FAUVE_H_INCLUDED
