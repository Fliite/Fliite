global monReseau
monReseau = {'A':[('B',4),('C',8)], 
            'B':[('A',4),('C',7),('D',12),('E', 21)], 
            'C':[('B': 7), ('A': 8), ('F': 25), ('D': 10)],
            'D':[('B', 12), ('G', 31),('E', 15), ('F', 12), ('C', 10)],
            'E':[('B', 21), ('D', 15), ('F', 10)],
            'F':[('C', 25), ('D', 12), ('E', 10)],
            'G':[('D', 31), ('F', 7), ('E', 17)],
            }

def ajouterNoeud(monReseau, noeud):
    if noeud not in monReseau:
        monReseau.update({noeud : []})
    else:
        print("Ce noeud existe déjà")

#entrer une liste de string
#les noeuds seront vides (sans voisins)
def ajoutListe_Noeuds(monReseau, liste):
    for i in liste:
        ajouterNoeud(monReseau, i)


def Ajout_arete(monReseau, noeud1, noeud2, poids=1):
    if noeud1 in monReseau and noeud2 in monReseau:
        monReseau[noeud1].append((noeud2, poids))
        monReseau[noeud2].append((noeud1, poids))
        return 1
    else:
        return -1

#retourne tous les noeuds du réseau
def listeNoeuds(monReseau):
    return [i for i in monReseau.keys()]

def voisins(monReseau, noeud):
    return [i[0] for i in monReseau[noeud]]

#retourne le poids de l'arete entre noeud1 et noeud2
def poids(monReseau, noeud1, noeud2):
    for i in monReseau[noeud1]:
        if i[0] == noeud2:
            return i[1]
    return -1

#supprime un noeud et ses aretes
def suppr_sommet(monReseau, noeud):
    if noeud in monReseau:
        for i in monReseau[noeud]:
            monReseau[i[0]].remove((noeud, i[1]))#supprime les aretes connectées au noeud
        del monReseau[noeud] #puis supprime le noeud
        return 1
    else:
        return -1

def suppr_arete(monReseau, noeud1, noeud2):
    if noeud1 in monReseau and noeud2 in monReseau:
        monReseau[noeud1].remove((noeud2, poids(monReseau, noeud1, noeud2)))
        monReseau[noeud2].remove((noeud1, poids(monReseau, noeud1, noeud2)))
        return 1
    else:
        return -1

def retourneAretes(monReseau):
    aretes = []
    for i in monReseau:
        for j in monReseau[i]:
            if (j[0], i) not in aretes:
                aretes.append((i, j[0]))
    return aretes

#retourne la liste des noeuds adjascents à un noeud
def noeuds_adjascents(noeud):
    return [i for i in noeud]