#include "Fauve.h"
#include <string>
using namespace std;

Fauve::Fauve(string nom, string espece, int age, string proiePreferee):
				Felin(nom,espece,age), m_proiePreferee(proiePreferee)
{
}

Fauve::~Fauve() {
}

string Fauve::sePresenter()
{
	string s="";
	s+=Felin::sePresenter();
	s+=" ma proie preferee est le " + m_proiePreferee + "\n";
	return s;
}

string Fauve::seNourrir()
{
	string s="";
	s+=Felin::seNourrir();
	s+=+ " un " + m_proiePreferee + "\n";
	return s;
}

string Fauve::seNourrir(string proieDuJour)
{
	string s="";
	s+=Felin::seNourrir();
	s+=+ " un " + proieDuJour + "\n";
	return s;
}
