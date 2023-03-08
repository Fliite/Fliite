D = { 1 : "z" ,2 : "a" ,45 : "z" ,12 : "ee" ,152 : "z" }

def dinverse():
    #retourne un dictionnaire dont les clés sont les valeurs de D et les valeurs les clés de D
    #si deux cles ont la meme valeur, on les met dans une liste
    #la valeur de la cle est cette liste
    Dinv = {}
    for i in D:
        if D[i] in Dinv:
            Dinv[D[i]].append(i)
        else:
            Dinv.update({D[i] : [i]})
    return Dinv

print(dinverse())
