pL1 = [1,4,3,5]
pL2 = [1,1,4,5,3]
pL3 = [5,1,2,3,8,-5,-4,7]
pL4 = [1,4,3,4,5,1,5,5]


def couples_consecutifs(pL):
#retourne liste de couples de valeurs consécutives successives dans pL
    l = []
    for i in range(len(pL)-1): 
        if pL[i] + 1 == pL[i+1]: #si valeur suivante est consécutive
            l.append((pL[i], pL[i+1])) #ajoute le couple des deux valeurs dans la liste
    return l

print(couples_consecutifs(pL1))
print(couples_consecutifs(pL2))
print(couples_consecutifs(pL3))

#retourne les valeurs de la liste en cle et le nombre de leurs occurences en valeur dans un dico
def nbOcc(pL):
    D = {}
    for i in pL: #pour chaque valeur de la liste
        if i in D:
            D[i] += 1 #si la valeur est déjà dans le dico, on ajoute 1 à sa valeur
        else:
            D[i] = 1 #sinon on l'ajoute avec une valeur de 1
    return D

print(nbOcc(pL4))