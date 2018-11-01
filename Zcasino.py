# -*-coding:Latin-1 -*
# Ce fichier abrite le code du ZCasino, un jeu de roulette adapté

import os
from random import randrange
from math import ceil

# Déclaration des variables de départ
argent = 1000 # On a 1000 $ au début du jeu
continuer_partie = True # Booléen qui est vrai tant qu'on doit
                        # continuer la partie

print("Vous vous installez à la table de roulette avec", argent, "$.\n")
nom = input ("quel est votre nom ? ")
while continuer_partie: # Tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur
    # lequel il va miser
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("\n %s, Tapez le nombre sur lequel vous voulez miser (entre 0 et 49) : "%nom) 
        # On convertit le nombre misé
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("%s, Vous n'avez pas saisi de nombre"%nom)
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("%s, Ce nombre est négatif"%nom)
        if nombre_mise > 49:
            print("Ce nombre est supérieur à 49")

    # À présent, on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
		
        mise = input(" %s, Tapez le montant de votre mise : "%nom)
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > argent:
            print("Vous ne pouvez miser autant, vous n'avez que", argent, "$")

    # Le nombre misé et la mise ont été sélectionnés par
    # l'utilisateur, on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("La roulette tourne... ... et s'arrête sur le numéro", numero_gagnant)

    # On établit le gain du joueur
    if numero_gagnant == nombre_mise:
        print("\n Félicitations ! Vous obtenez", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("\n Vous avez misé sur la bonne couleur. Vous obtenez", mise, "$")
        argent += mise
    else:
        print("\n Désolé %s, c'est pas pour cette fois. Vous perdez votre mise."%nom)
        argent -= mise
	
    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("\n % s, Vous êtes ruiné ! C'est la fin de la partie."%nom)
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", argent, "$")
        quitter = input("\n Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False

# On met en pause le système (Windows)
os.system("pause")