import random

def liste_random_croissante(length, start, end):
    liste = []
    for i in range(length):
        liste.append(random.randint(start, end))
    liste.sort()
    return liste

Liste = liste_random_croissante(50, -100, 200)
x = random.randint(-100, 200)

def dichotomie(liste,x):
    i = len(liste)//2
    if liste[i] < x:
        i = i + len(liste)//2
    elif liste[i] == x:
        return True, i
    else:
        i = i - len(liste)//2

print(dichotomie(Liste), Liste)