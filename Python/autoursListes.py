# -*- encoding: utf8 -*-

import time

def p1_isPrime(num):
    """
    A function to answer if a number is "premier".

    """  
    num = int(num)
    #debug print(num)
    if num < 2: 
        return False
    else:
        if num > 2 and num % 2 == 0:
            return False
        for x in range(2, num // 2):
            if num % x == 0:
                return False
        return True

def p2_listeCreate(n):
    li = [i for i in range(n)]
    return li

def p3_quePremiers(listeatraiter):
    nbitem=len(listeatraiter)
    #debug print(nbitem)
    listebase=p2_listeCreate(nbitem)
    #print(listebase)
    listpremiers = []
    for i in listebase:
        if p1_isPrime(i):
           listpremiers.append(i)
    return listpremiers

def p4_2_rang(r):
    return p3_quePremiers(p2_listeCreate(r))

step = 10000
i = step
print("+-----------+---------------------|")
print("|  rang     |  Temps d'exécution  |")
print("+-----------+---------------------|")
for i in range (10000,200000,step):
    start_time = time.time()
    p4_2_rang(i)
    interval = time.time() - start_time
    #print("| ",i, "  | ",interval," secondes |")
    print("| ",i, "  |  {:>4f}  secondes  |".format(interval))
    #print("{:>5f} n'est pas un nombre premier!".format(interval))
print("+-----------+----------------------|")

