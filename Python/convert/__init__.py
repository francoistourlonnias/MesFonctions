import os

def dechex(deci):
    def quinze(nb):
        base = 16
        div=nb
        Q=div/base
        r=div%base
        print ( Q, r)
        if r>9:
            if r==10:
                r="A"
            else:
                if r==11:
                    r="B"
                else:
                    if r==12:
                        r="C"
                    else:
                        if r ==13:
                            r="D"
                        else:
                            if r ==14:
                                r="E"
                            else:
                                r="F"
        return r
    if deci <= 15:
        return quinze(deci)
    else:
        print("trop grand")


def hexdec():
    i=1
def bd(b):
    #print ("on veux convertir: ",b)
    #decoupe en containers de 4 caracteres
    y=len(b)
    #debug print (x)
    #ici verif des caracteres en patant du dernier
    if (y % 4) == 0: #dans ce cas le nbre de container est le resultat de la division
        nbcontain= int(y / 4)
        #debug print ("nombre de container modulo",nbcontain)
    else:
        nbcontain= int(y / 4)+1
        #debug print ("nombre de container divi",nbcontain)

    #print("nbre de container",nbcontain)
    #maintenat il faut remplir les containers en partant de la fin et combler avec 0 si il y a des vides dans le dernier
    vide = [0,0,0,0]
    mot = vide * nbcontain
    idxm= (4*nbcontain)-1
    idxb= y-1
    while idxb >= 0:
        mot[idxm]=b[idxb]
        idxm-=1
        idxb-=1
        
    #ici le mot est remplis et complete a gauche   
    print ("mot",mot)
    res = 0
    idx= len(mot)
    #print(idx)
    p=0
    while idx >0:
        
        anti= len(mot)-idx
        res= res+ int(mot[idx-1])*(2**p)
        #print ("debug mot ",mot[idx-1],"puissance ",p, "res ",res)
        p+=1
        idx-=1
        
    #print(res) 
    return res                            
def db():
    n=0
    n=input("choisir un nombre que vous voulez convertir en binaire:")
    n=int(n)
    container=[]
    while ( n != 0):
        s=n % 2
        if (s == 0):
            container.append("0")
        else :
            container.append("1")
        n= n//2
    container.reverse()
    return container

def saisie ():
    s=input("Tapez le nombre binaire dont vous desirez la conversion (serie de 0 et 1) :")
    #print ("votre saisie:",s)
    x=len(s)
    #ici verif des caacteres en patant du dernier
    while x >=0:
        #une chaine commence a 0
        if int(s[x-1]) != 1 and int(s[x-1])!=0: 
            print ("erreur de saisie",s[x-1]," n'est pas un chiffre binaire" )
            exit(1)
        x-=1
    nbc=len(s)   
    return (s,nbc)

#MAIN

charlotte=db()
print(charlotte)
#sais,taille=saisie()
#deci=bd(sais)
#print ("deci",deci)

#q1,r1=dechex(deci)
#print (q1,r1)


#print(dechex(deci))
#print (q2,r)
#print (q1,r1,q2,r2)
    

    