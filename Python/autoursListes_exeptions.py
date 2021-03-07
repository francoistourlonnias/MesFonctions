# -*- encoding: utf8 -*-
class LowerThanTwo(Exception):
    pass

def isPrime(num):
    """
    A function to answer if a number is "premier".

    """  
    try:
        num = int(num)
        if num < 2: raise LowerThanTwo()
    except ValueError:
        return False, "Saisir un nombre valide 0 et 1 ne répondent pas à la définition, ils ne sont donc pas des nombres premiers !!!"
    except LowerThanTwo:
        return False, "Saisir un nombre supérieur égal à 2 !!!"
    else:
        if num > 2 and num % 2 == 0:
            return False, "{:>5d} n'est pas un nombre premier!".format(num)
        for x in range(2, num // 2):
            if num % x == 0:
                return False, "{:>5d} n'est pas un nombre premier!".format(num)
        return True, "{:>5d} est un nombre premier!".format(num)

listebase = [i for i in range(11)]
print(listebase)
for i in listebase:
    print ( i,isPrime(i))
    listpremiers = [isPrime(i) == True for i in listebase]
print(listpremiers)