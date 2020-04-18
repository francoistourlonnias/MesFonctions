//============================================================================
// Name        : Heritages.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include "Heritages.h"

//constructeur
Felin::Felin(std::string nom,  std::string espece, int age):
m_nom(nom),m_espece(espece),m_age(age)
{
}

//methode
std::string Felin::seNourrir()
{
	std::string res= " Je mange " ;
	return res;
}
std::string Felin::sePresenter()
{
	std::string res= " Je suis " + m_nom + " j ai "+ to_string(m_age) + " ans, je suis un " + m_espece ;
	return res;
}
//=====================================================================================================================
ChatSauvage::ChatSauvage(std::string nom,  std::string espece, int age,std::string proiePreferee ):
Felin(nom,espece,age),m_proiePreferee(proiePreferee)
{
}
//methode


std::string ChatSauvage::seNourrir()
{
	std::string res= Felin::seNourrir() + m_proiePreferee ;
	return res;
}
std::string ChatSauvage::sePresenter()
{
	std::string res= Felin::sePresenter() +"ma proie preferee est" + m_proiePreferee;
	return res;
}
//=====================================================================================================================
ChatDomestique::ChatDomestique(std::string nom,  std::string espece, int age,std::string proiePreferee,std::string couleurCollier ):
Felin(nom,espece,age),m_proiePreferee(proiePreferee),m_couleurCollier(couleurCollier)
{
}
//methode
std::string ChatDomestique::seNourrir()
{
	std::string res= Felin::seNourrir() + m_proiePreferee ;
	return res;
}
std::string ChatDomestique::sePresenter()
{
	std::string res= Felin::sePresenter() +"la couleur de mon collier est " + m_couleurCollier;
	return res;
}
//========================================================================================================================
int main() {

	Felin Chat ("Felix","chat",5);

	cout << Chat.sePresenter();

	ChatSauvage C1 ("CS1","chat sauvage ",10,"le mulot");
	cout << endl << C1.sePresenter();
	cout << endl << C1.seNourrir();

	ChatDomestique C2 ("CS2","chat Domestique ",20," des croquettes"," Indigo");
	cout << endl << C2.sePresenter();
	cout << endl << C2.seNourrir();

}
