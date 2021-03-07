# -*-coding:Latin-1 -*
liste = ["a","d","m"]

cpt=len(liste)
for i in range(0,cpt):
    print(liste[i])

def ma_fiche(prenom, nom, *reste):
#def ma_fiche(**parametres):
    return prenom + " " + nom 

a = ma_fiche("olivier","engel","tsooin tsoin")
print (a)


#if __name__ == "__main__" :
        