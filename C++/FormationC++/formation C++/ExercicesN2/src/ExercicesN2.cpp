//============================================================================
// Name        : ExercicesN2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
using namespace std;


string motAleatoire()
{

	string res;
	for (int cpt=0; cpt<6;cpt++)
	{
	char C = rand() % 26 + 'A';

	res+=C;
	//cout << C; << endl;
	}

	return res;
}



int main() {
	cout << "Tableaux et Methodes" << endl; // prints Tableaux et Methodes

	srand(time(0)); //timestamp de maintenant
	cout << motAleatoire();

	vector <string> tableauAleatoire (25);
	for (int cpt=0; cpt<24;cpt++)
	{
		//tableauAleatoire.push_back();
		tableauAleatoire[cpt]=motAleatoire();
	}

	for (int cpt=0; cpt<24;cpt++)
	{
	cout << tableauAleatoire[cpt];
	cout << endl;
	}



	return 0;
}
