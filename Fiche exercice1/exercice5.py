Dupont = " 10/6 -25.0 15/6 -5.0 22/6 -35.0 30/6 93.50 4/7 -10.0 8/7 -10.0 15/7 -5.0 15/7 -15.0 20/7 11.50 "

def extraire(chaine):
    for i in len(chaine):
        L = []
        if chaine[i] == " ":
        #on ajoute tous les string etre l'index i et i-e
            strint = chaine[i-e:i]
            L.append(strint)
            pass
        else:
            e+=1
    return L

print(extraire(Dupont))