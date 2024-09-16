# variables test 
Rackam1 = [[50, "n"], [20, "e"], [30, "s"], [45, "o"], [12, "s"], [80, "o"], [63, "s"], [48, "s"], [12,"o"], [3,"o"], [8, "n"]]
Dupont = "10/6 -24 15/6 -5 22/6 -35 30/6 93.5 4/7 -10 8.7 -10 15/7 -5 15.7 -15 20/7 11.5"
######


def rackam(liste):
    #renvoie la liste des direcion positives (nord et est)
    for i in range(len(liste)):
        sumN = sumE = sumS = sumO = 0
        if liste[i][1] == "n":
            sumN += liste[i][0]
        elif liste[i][1] == "e":
            sumE += liste[i][0]
        elif liste[i][1] == "s":
            sumS += liste[i][0]
        else:
            sumO += liste[i][0]
        
        liste = [[sumN, "n"], [sumE, "e"], [sumS, "s"], [sumO, "o"]]

    return liste

def Flavius(N, P):
        personnes = list(range(1, N + 1))
        index = 0
        liste = []

        while len(personnes) > 1:
            liste.append(personnes[index])
            personnes.pop(index)
            index = (index + (P-1)) % len(personnes)
        return liste

def Hamming(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Les deux séquences doivent avoir la même longueur")
    else:
        l = []
        listePos = []
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                l.append(seq1[i])
                listePos.append(i)
        return len(l), listePos

def MemeVal(liste1, liste2):
    same = []
    b = True
    for i in liste1:
        if i in liste2:
            same.append([i, True])
        else:
            same.append([i, False])
            b = False
    return b

def MemeVal2(str1, str2):
    same = []
    for i in str1:
        if i in str2:
            same.append([i, True])
        else:
            same.append([i, False])
    return same

def PermutListe(liste1, liste2):
    if len(liste1) != len(liste2):
        raise ValueError("Les deux listes doivent avoir la même longueur")
    elif MemeVal(liste1, liste2) == False:
        raise ValueError("Les deux listes doivent contreir les mêmes éléments") 
    else:
        l1 = liste1.copy()
        l2 = liste2.copy()
        compteur = 0
        #compter le nombre de permutation sur l1 pour obtenir l2
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                l1[i], l1[l1.index(l2[i])] = l1[l1.index(l2[i])], l1[i]
                compteur += 1

        return compteur

def bookmaker(str):
    liste = str.split()
    lesDates = [i for i in liste if "/" in i]
    lesSommes = [i for i in liste if "/" not in i]
    Solde = sum([float(i) for i in lesSommes])
    OpeSeptembre = len([i for i in lesDates if i.split("/")[1] == "7"])

    return Solde, OpeSeptembre

def CaracSolitaire(str):
    liste = list(str)
    print(liste)
    for i in [1,range(liste)-1]:
        if liste[i] != liste[i-1] or liste[i] != liste[i+1]:
            liste.pop(i)
        chaine = "".join(liste)
    return liste

# appel des foncions
#print("Rackam",rackam(Rackam1))
#print("Flavius", Flavius(41, 4))
#print("Hamming", Hamming("101010", "111010"))
#print("MemeVal", MemeVal([1, 2, 3, 4, 5, 4], [2, 4, 6, 8, 10, 4]))
#print("MemeVal2", MemeVal2("12345", "246810"))
#print("PermutListe", PermutListe([1, 2, 3, 4, 5], [2, 4, 1, 5, 3]))
#print("bookmaker", bookmaker(Dupont))
print(CaracSolitaire("aasrffzrrrzzdttl"))