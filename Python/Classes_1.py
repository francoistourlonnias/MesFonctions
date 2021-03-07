# -*-coding:Latin-1 -*
class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self): # Notre méthode constructeur
        """Constructeur de notre classe. Chaque attribut va être instancié
        avec une valeur par défaut... original"""
        self.nom = "Dupont"
        self.prenom = "Jean" # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"


if __name__ == "__main__" :
    quidam=Personne()
    quidam.age=54
    print (quidam.nom)
    print (quidam.age)

    FTS=Personne()
    FTS.lieu_residence = "Chartres"
    FTS.nom = "Fritz"
    print (FTS.nom)
    print (FTS.lieu_residence)