/*
 * main.cpp
 *
 *  Created on: 21 sept. 2016
 *      Author: ftourlon
 */

#include <iostream>
#include "Felin.h"
#include "ChatSauvage.h"
#include "ChatDomestique.h"

using namespace std;
int main() {

	Felin Chat ("Felix","chat",5);

	cout << Chat.sePresenter();

	ChatSauvage C1 ("CS1","chat sauvage ",10,"le mulot");
	cout << endl << C1.sePresenter();
	cout << endl << C1.seNourrir();

	ChatDomestique C2 ("CS2","chat Domestique ",20," des croquettes"," Indigo");
	cout << endl << C2.sePresenter();
	cout << endl << C2.seNourrir();

	return 0;
}
