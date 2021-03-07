class Vehicule:
    
    couleur = 'indigo'
    
class AnalyseurSpectre:
    
    couleur = 'blanc'
    
    def __init__(self, couleur=None, identifiant=None):
        self.identifiant = identifiant
        if couleur is None:
            self.couleur = Vehicule.couleur
        else:
            self.couleur = couleur
            
    def afficher(self):
        print("Identifiant: %s" % self.identifiant)
        print("Couleur: %s" % self.couleur)
            
#class HP8566(AnalyseurSpectre):
#    pass

class HP8566(AnalyseurSpectre):

    def __init__(self, port_usb='usb3', couleur=None, identifiant=None):
        super(HP8566, self).__init__(couleur, identifiant)
        #AnalyseurSpectre.__init__(self, couleur, identifiant)
        self.port_usb = port_usb


voit1 = HP8566()
voit2 = HP8566("rouge", "SN 1234")
voit2.afficher()


as1 = HP8566()
as1.afficher()
as2 = HP8566("rouge", "sn1234")
as2.afficher()

#if __name__ == "__main__" :
#    table(10)
#    os.system("pause")