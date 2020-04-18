//test_factorial.cpp
/* resultats des utilisations de methodes
 *
 Je suis Felix j ai 5 ans, je suis un chat
 Je suis CS1 j ai 10 ans, je suis un chat sauvage ma proie preferee estle mulot
 Je mange le mulot
 Je suis CS2 j ai 20 ans, je suis un chat Domestique la couleur de mon collier est  Indigo
 Je mange  des croquettes
 */

# include "gtest/gtest.h"
#include "../src/Felin.h"
#include "../src/ChatSauvage.h"
#include "../src/ChatDomestique.h"

using namespace std;

TEST (testdeFelin, Inst){

	//instanciation de l'objet
	Felin Chat ("Felix","chat",5);

	//check du resultat
	EXPECT_EQ("Je suis Felix j ai 5 ans, je suis un chat", Chat.sePresenter());
}


