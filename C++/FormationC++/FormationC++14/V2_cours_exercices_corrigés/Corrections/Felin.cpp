#include <iostream>
#include "Felin.h"

using namespace std;

Felin::Felin(string nom, string espece, int age):
    m_nom(nom),m_espece(espece),m_age(age)
    {
    }

string Felin::sePresenter()
{
    string s = "";
    s+= "Je suis " + m_nom + " j'ai "+ to_string(m_age) + " ans et je suis un "+ m_espece +"\n";
    return s;
}

string Felin::seNourrir()
{
    string s = "";
    s+= "Je mange";
    return s;
}
