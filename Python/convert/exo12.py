# -*- encoding: utf8 -*-
m=mp=10000
deb=0.5 #cm
raison=2
fin=int(input("entrez la fin:"))

print ("m :",m," m' :",mp, " deb: ",deb,"fin: ",fin," raison",raison)

r=[]
r.append(deb)
cpt=0
while cpt < (fin-1):
    r.append(r[cpt]*raison)
    cpt+=1

print(r)
idx=1
while idx <= (len(r)-1):
    delta=r[idx]-r[idx-1]
    f=(6.67*10**(-11)*m*mp)/((delta)**2)
    #print(delta, f)
    #print ( "d :", float(delta),"m : la force vaut :", f, " N")
    print ("d : {:.2f} m : la force vaut : {:.4f} N ".format (delta,f*100))

    idx+=1


