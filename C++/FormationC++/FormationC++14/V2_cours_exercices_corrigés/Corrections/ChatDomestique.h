#ifndef CHATDOMESTIQUE_H_INCLUDED
#define CHATDOMESTIQUE_H_INCLUDED

#include "Felin.h"
#include <string>

class ChatDomestique: public Felin {
public:
	ChatDomestique(std::string nom, std::string espece, int age, std::string couleurCollier);
	virtual ~ChatDomestique();
	std::string sePresenter();
	std::string seNourrir();
private:
	std::string m_couleurCollier;
};

#endif // CHATDOMESTIQUE_H_INCLUDED
