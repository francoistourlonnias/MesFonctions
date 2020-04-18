//============================================================================
// Name        : Cours.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Animal
{
	//Attributs
	string m_nom;
	string m_espece;
	int m_age;

	public:

	//constructeur

		//	Animal(string nom,string espece,int age)
		//		{
		//			m_nom =nom;
		//		m_espece=espece;
		//		m_age=age;
		//		}
	Animal(string nom,string espece,int age):m_nom(nom),m_espece(espece),m_age(age)
	{

	}
	//destructeur
	~Animal() {}

	//Autre methode
	void saluer()
	{
		cout << "Bonjour ! je suis " << m_nom << endl;
		cout << "je suis un " << m_espece << " et j'ai ";
		cout << m_age << " ans.";
	}
};
