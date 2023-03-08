D = { 1 : "z" ,2 : "a" ,45 : "AAA " ,12 : "ee" ,152 : "Bac" }

def dinverse():
    #retourne un dictionnaire dont les clés sont les valeurs de D et les valeurs les clés de D
    Dinv = {}
    for i in D:
        Dinv.update({D[i] : i})
    return Dinv

print(dinverse())