stock = [["Humex rhume", 25, 3.50],["Nurofen", 5, 3.50], ["Rhinureflex", 64, 4.20]]

def ajouterRefMedicament(pS, pM):
    if pM in pS:
        return False
    else:
        pS.append([pM, 0, 0])
        return True, pS

print(ajouterRefMedicament(stock, 'antibiotiques'))

def vendreMedicament(pS, pM, pN):
    for i in range(len(pS)):
        if pS[i][0] == pM: #si le médicament est dans le stock
            if pS[i][1] < pN:
                return False, "Il n'y a pas assez de médicaments dans le stock"
            elif pS[i][1] == pN: #si on vend tous les médicaments du stock
                pS.pop(i)
                return True, pS
            else: #si le stock n'est pas vide
                pS[i][1] -= pN
                return True, pS
        else:
            return False, "Le médicament n'est pas dans le stock"
    

print(vendreMedicament(stock, 'Humex rhume', 24))

def valeurStock(pS):
    #retourne la valeur du stock
    valeur = 0
    for i in range(len(pS)):
        valeur += pS[i][1] * pS[i][2]
    return valeur

print("le stock vaut", valeurStock(stock))