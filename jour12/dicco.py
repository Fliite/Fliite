def est_Premier(n):
    #Renvoie True si n est premier, False sinon
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def premiers(n):
    #Renvoie la liste des nombres premiers inférieurs ou égaux à n
    liste = []
    for i in range(2, n + 1):
        if est_Premier(i):
            liste.append(i)
    return liste

def demande():
    #demande une liste d'entiers
    listed = []
    while True:
        n = int(input("Entrez un entier positif: "))
        if n <= 0: #stop si négatif
            break
        listed.append(n)
    return listed

def rentre_dans_dico(liste):
    #Renvoie un dictionnaire avec les nombres de l'utilisateur comme clés 
    #et les nombres de la liste de premiers comme valeurs
    dico = {}
    for i in liste:
        dico.update({i : premiers(i)})
    return dico

print(rentre_dans_dico(demande()))