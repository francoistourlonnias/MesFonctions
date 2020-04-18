/*
 * main.cpp
 *
 *  Created on: 20 sept. 2016
 *      Author: ftourlon
 */
#include "ExerciceObjects.h"
using namespace std;
int main() {
	Appartement francois (7,190,"blanc","carrelage");

	cout << francois.description();

	francois.changer_sol();

	cout << francois.description();

	return 0;
}


