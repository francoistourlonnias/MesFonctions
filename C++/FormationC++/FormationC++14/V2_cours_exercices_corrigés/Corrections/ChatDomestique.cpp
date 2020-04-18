#include "ChatDomestique.h"
#include <string>
using namespace std;

ChatDomestique::ChatDomestique(string nom, string espece, int age, string couleurCollier):
Felin(nom,espece,age), m_couleurCollier(couleurCollier)
{
}

ChatDomestique::~ChatDomestique() {
}

string ChatDomestique::sePresenter()
{
	string s="";
	s+=Felin::sePresenter();
	s+=" mon colier est " + m_couleurCollier + "\n";
	return s;
}

string ChatDomestique::seNourrir()
{
	string s="";
	s+=Felin::seNourrir();
	s+=+ " des croquettes \n";
	return s;
}
