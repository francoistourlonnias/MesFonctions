//============================================================================
// Name        : training.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <memory>
#include <algorithm>

#include "Apartment.hpp"
#include "Couch.hpp"
using namespace std;

int main() {
	Apartment myApartment;
	Couch myCouch;

	cout << "************** Apartment ******************" << endl;

	cout << myApartment.description();
	myApartment.paint("grey");
	cout << myApartment.description();
	cout << endl;
	cout << myCouch.description();
	myApartment.setCouch(&myCouch);
	cout << myApartment.description();

	myCouch.setColor("red");
	cout << myApartment.description();

	// Copy constructor
	cout << "************** Copy Constructor ******************" << endl;
	Apartment newApartment(myApartment);
	Couch newCouch;

	myCouch.setColor("white");
	cout << myApartment.description();
	cout << newApartment.description();
	newApartment.setCouch(&newCouch);
	cout << newApartment.description();


	cout << "************** Exceptions ******************" << endl;
	try {
		Apartment tooSmallApartment(8);
	}
	catch (std::exception const& e){
		cerr << e.what() << endl;
	}

	cout << "************** Shared Pointer ******************" << endl;
	std::shared_ptr<Couch> pIkeaCouch(new Couch);
	pIkeaCouch->setColor("blue");
	cout << newApartment.description();

	Apartment myApartmentWithCouch(6,"cordura","pale green");
	cout << myApartmentWithCouch.description();

	cout << "************** Operator Overload ******************" << endl;

	if(myApartmentWithCouch==newApartment)
		cout << "Apartments are equal" <<endl;
	else
		cout << "Apartments are different"<< endl;

	Apartment bigApartmentOne(250);
	Apartment bigApartmentTwo(250);

	if(bigApartmentOne==bigApartmentTwo)
		cout << "Apartments are equal" <<endl;
	else
		cout << "Apartments are different"<< endl;

	return 0;
}
