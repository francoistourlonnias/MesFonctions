//============================================================================
// Name        : SurchargeOperateurs.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include "Duree.h"
using namespace std;

int main() {

	//test pour voir
	Duree hour  (10,30,5);
	Duree hour2 (10,20,5);


	hour.affichage() ; // prints Tableaux et Methodes

	cout << hour.estEgal(hour)  << endl;
	cout << hour.estEgal(hour2) << endl;

	//utilisation de la surcharge pour faire la meme chose:
	cout << "operateor== " << operator==(hour,hour2) << endl;
	//ajouts

	Duree hour3 = operator+(hour,hour2) ;
	hour3.affichage();



	Duree hour4 = operator-(hour3,hour2) ;
	hour4.affichage();


	cout << operator==(hour,hour4) << endl;

	hour4.operator+=(hour4);
	hour4.affichage();

	cout << "h < h2 " << operator<(hour,hour2) << endl;
	return 0;
}
