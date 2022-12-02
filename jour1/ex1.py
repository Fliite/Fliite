from random import randint

def liste_hasard(val):
    var = randint(0,val)
    liste = []
    liste.append(var)
    return(liste)

print(liste_hasard(100))
