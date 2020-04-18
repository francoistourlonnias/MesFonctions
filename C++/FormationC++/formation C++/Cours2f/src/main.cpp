/*
 * main.cpp
 *
 *  Created on: 23 sept. 2016
 *      Author: ftourlon
 */
#include "Cours2f.hpp"
#include "Oiseau.hpp"
#include <vector>
#include <memory> //pour les shared_ptr
#include <iostream>

using namespace std;

int main()
{
	Animal max("Max","Okapi",7);
	max.saluer();
	max.setAge(70);
	max.saluer();

	Oiseau canari("Titi","oiseau",2,"ma cage");
	canari.saluer();
	canari.voler();

	Animal leon("Leon");
	leon.saluer();

	//polymorphisme
	//creation d'un vecteur d'Annimaux  slide 43 et 111
	vector<Animal> vec = {max,canari};

	//demande aux animaux de saluer
//	for (int i=0;i<vec.size();i++)
//		vec[i].saluer();
//
	shared_ptr<Animal> pmax;
	pmax = make_shared<Animal>("Max","okapi",7);
	shared_ptr<Oiseau> pbea;
	pbea= make_shared<Oiseau>("Veatrice","Perdrix",3,"Le Grand Chene");
	vector<shared_ptr<Animal>> pvec {pmax,pbea};
	for (int i=0;i<pvec.size();i++)
			pvec[i]->saluer();
	return 0;
}


