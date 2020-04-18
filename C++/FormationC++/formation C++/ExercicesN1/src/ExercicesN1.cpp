//============================================================================
// Name        : ExercicesN1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int annee = 2016 ;
	string  bonjour = "Hello " , monde = " World ";
	cout << bonjour << monde << annee  << endl; // prints !!!Hello World!!!

	string nouvelle = "42";
	cout << annee + stoi(nouvelle);

	int x,y ;
	cout << "entrer la valeur pour X \n";
	cin >> x;
	cout << "entrer la valeur pour y \n";
	cin >> y;
	cout << x;
	cout << y;
	for ( int cpt=0; cpt <=y ;cpt+=x)
	{
		cout << cpt << endl;
	}
	string etoile, lf="\n";
	for ( int cpt=0; cpt <10 ;cpt+=x)
	{
		etoile+="*";
		//cout << etoile << endl;
		cout << etoile + lf;
	}
cout << lf+lf+lf;

	for ( int cpt=0; cpt <10 ;cpt+=x)
	{
		for ( int cp=0; cp <10 ;cp+=x)
		{
		etoile="*";
		cout << etoile ;
		}
		cout << lf;
	}

	double int1=13, int2=5;
	cout << int1 / int2;


	// losange  a terminer
	cout << lf+lf+lf;

		for ( int cpt=0; cpt <10 ;cpt+=x)
		{
			for ( int cp=0; cp <10 ;cp+=x)
			{
			etoile="*";
			cout << etoile ;
			}
			cout << lf;
		}
	return 0;
}
