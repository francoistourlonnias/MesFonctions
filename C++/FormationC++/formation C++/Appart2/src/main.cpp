/*
 * main.cpp
 *
 *  Created on: 20 sept. 2016
 *      Author: ftourlon
 */
#include "ExerciceObjects.h"
using namespace std;
int main() {

	//raw Canape chmulbluck (4,"fleurs","blanc");
	//raw Appartement francois (7,190,"blanc","carrelage",&chmulbluck);


	shared_ptr<Canape> chmulbluck = make_shared<Canape>(4,"fleurs","blanc");
	Appartement francois (7,190,"blanc","carrelage",chmulbluck);

	cout << francois.description() << endl;

	francois.changer_sol();

	cout << francois.description() << endl;


	// raw cout << chmulbluck.descriptionCanape() << endl;
	cout << chmulbluck->descriptionCanape() << endl;

	return 0;
}


