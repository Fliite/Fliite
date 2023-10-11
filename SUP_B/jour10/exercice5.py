L1 = {'A':-5 , 'C':10 , 'Z':-3 , 'T':4, 'M':2 , 'E':1}
L2 = {'C':-5 , 'A':5 , 'U':45 , 'N':8, 'T':12 , 'Z':1}

def fusion():
    # fusionne les deux dico en sommant les valeurs des clés communes
    # si la somme est nulle, la clé est supprimée
    dico = L1
    for i in L2:
        if i in dico:
            dico[i] += L2[i]
            if dico[i] == 0:
                del dico[i]
        else:
            dico.update({i : L2[i]})
    return dico

print(fusion())