M = [[4,5,9],[9,1,2,],[6,7,4]]

def estCarre(M):
    for i in range(len(M)):
        if len(M[i]) != len(M):
            return False
    return True


def estMagique(M):
    #somme des lignes
    for i in range(len(M)):
        somme_L = 0
        for j in range(len(M[i])):
            somme_L += M[i][j]
    #somme des colonnes
    for i in range(len(M)):
        somme_C = 0
        for j in range(len(M[i])):
            somme_C += M[j][i]
    #somme des diagonales
    somme_D = 0
    for i in range(len(M)):
        somme_D += M[i][i]
    #évaluation des sommes
    if somme_L == somme_C == somme_D:
        return True

def main(M):
    if estCarre(M) == True:
        print("la matrice est carrée")
        if estMagique(M) == True:
            print("la matrice est magique")
    else:
        print("la matrice n'est pas carrée")