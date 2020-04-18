#include <iostream>
#include <cstdlib>
#include <ctime>
#include <memory>
#include <vector>
#include <map>
#include <algorithm>

#include "Appartement.h"
#include "Canape.h"
#include "Felin.h"
#include "Fauve.h"
#include "ChatDomestique.h"
#include "Duree.h"


using namespace std;


string genererMot()
{
    char c;
    string s = "";
    int i;

    //On crée autant de lettres aléatoires que désiré
    for(i = 0;i < 7;i++)
    {
        c = rand() % 26 + 'A';
        s += c;
    }

    //On retourne le mot créé
    return s;
}

vector<string> genererTableauMots()
{
    vector<string> v;
    for(int i = 0;i < 25;i++)
        v.push_back(genererMot());
    return v;
}

int main()
{
    //Exercice Mots Aléatoires
    cout << "**************** Exercice Mots Aleatoires *******" << endl << endl ;
    //On initialise le rand()
    srand(time(0));
    vector<string> vecteurDeMots = genererTableauMots();
    for(int i = 0; i < vecteurDeMots.size(); i++)
        cout << vecteurDeMots[i] << endl;

    //Exercice Appartement
    cout << endl << "**************** Exercice Appartement *******" << endl << endl;
    shared_ptr<Canape> canap = make_shared<Canape>(4, "Losanges", "Ecarlate");
    Appartement appart(2, 45, "Violet", "Carrelage", canap);
    cout << appart.description();
    appart.repeindre("Jaune");
    appart.remplacerCanape(8, "Psychedelique", "Arc en Ciel");
    cout << appart.description();

	try {
		Appartement appartTropPetit(1, 6, "Moisi", "Crottes de rats", canap);
	}
	catch (std::exception const& e){
		cerr << e.what() << endl;
	}

	//Exercice Felins
    cout << endl << "**************** Exercice Felins *******" << endl << endl;
    /* Ne fonctionne plus car classe abstraite
    Felin tigrou("Tigrou","Tigre de dessin anime",3);
    cout << tigrou.sePresenter();
    */
    cout << "Fauve et ChatDomestique seuls" << endl;
    Fauve sherkan("Sherkan","Tigre",13,"Buffle");
    cout << sherkan.sePresenter();
    cout << sherkan.seNourrir();
    cout << sherkan.seNourrir("Antilope");
    ChatDomestique tigrounet("Tigrounet","Chaton Tigre",1,"Rose");
    cout << tigrounet.sePresenter();
    cout << tigrounet.seNourrir();
    cout << "Fauve et ChatDomestique en polymorphisme" << endl;
    vector<shared_ptr<Felin>> porteChats = {
    make_shared<Fauve>("Sherkan","Tigre",13,"Buffle"),
    make_shared<ChatDomestique>("Tigrounet","Chaton Tigre",1,"Rose")
    };
    for(int i = 0; i<porteChats.size(); i++)
        cout << porteChats[i]->sePresenter();

	//Exercice Durees
	cout << endl << "**************** Exercice Durees *******" << endl << endl;
    Duree parisLyon(2,13,13);
	Duree lyonTurin(3,18,12);
	Duree parisLondres(2,33,23);


	cout << "Vector" << endl;
	vector<Duree> dureeTrajets;
	vector<Duree>::iterator dureeTrajetsIt;

	dureeTrajets.push_back(parisLyon);
	dureeTrajets.push_back(lyonTurin);
	dureeTrajets.push_back(parisLondres);

	for (dureeTrajetsIt=dureeTrajets.begin(); dureeTrajetsIt!=dureeTrajets.end();dureeTrajetsIt++)
	{
		cout << (*dureeTrajetsIt).affiche();
	}

	cout << "Map" << endl;
	map<string, Duree> trajets;
	trajets.insert(pair<string,Duree>("Paris Lyon",parisLyon));
	trajets.insert(pair<string,Duree>("Lyon Turin",lyonTurin));
	trajets.insert(pair<string,Duree>("Paris Londres",parisLondres));

	map<string, Duree>::iterator trajetsIt;

	for (trajetsIt=trajets.begin();trajetsIt!=trajets.end();trajetsIt++)
	{
		cout << (*trajetsIt).first << " " << (*trajetsIt).second.affiche();
	}
	cout << endl;


	cout << "Tri de vecteur avec foncteur" << endl;

	class compareDuree{
	public:
		bool operator() (Duree d1, Duree d2)
		{
			return !(d1<d2);
		}
	};

	sort(dureeTrajets.begin(),dureeTrajets.end(),compareDuree());

	for (trajetsIt=trajets.begin();trajetsIt!=trajets.end();trajetsIt++)
	{
		cout << (*trajetsIt).first << " " << (*trajetsIt).second.affiche();
	}
	cout << endl;


	cout << "Affichage de map avec boucle automatique" << endl;

	for(auto curseur:trajets)
	{
		cout << curseur.first << " " << curseur.second.affiche();
	}

	cout << "Tri de vector avec lambda" << endl;

	auto lambdaCompare = [](Duree d1, Duree d2){return (d1<d2);};

	sort(dureeTrajets.begin(),dureeTrajets.end(),lambdaCompare);

	for (auto curseur:dureeTrajets)
	{
		cout << curseur.affiche();
	}

	return 0;
}


