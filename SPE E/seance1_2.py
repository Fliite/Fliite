# variables test 
Rackam1 = [[50, "n"], [20, "e"], [30, "s"], [45, "o"], [12, "s"], [80, "o"], [63, "s"], [48, "s"], [12,"o"], [3,"o"], [8, "n"]]
Dupont = "10/6 -24 15/6 -5 22/6 -35 30/6 93.5 4/7 -10 8.7 -10 15/7 -5 15.7 -15 20/7 11.5"
Code1L = "ACDEFGHIKLMNPQRSTVWY"
Code3L = Code3L = ["ALA" , "CYS" , "ASP" , "GLU" , "PHE" , "GLY" , "HIS" , "ILE" , "LYS" , "LEU" , "MET" , "ASN"
, "PRO" , "GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"] 
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
    #Ecrire une fonction qui reçoit une chaîne de caractères et élimine chaque caractère qui est different du precedent ou du suivant
    l = []
    for i in range(len(str)):
        if i == 0:
            if str[i] == str[i+1]:
                l.append(str[i])
        elif i == len(str) - 1:
            if str[i] == str[i-1]:
                l.append(str[i])
        else:
            if str[i] == str[i+1] or str[i] == str[i-1]:
                l.append(str[i])
    return "".join(l)

def GrandeSequence(liste):
    #Écrire une fonction qui retourne la longueur de la séquence de valeurs croissantes dans une liste de valeurs entières
    #on mesure la longeur de la sequence ou les valeurs sont strictement croissantes
    l = []

def PivoterListe(liste, i, j):
    if i >= j or j > len(liste):
        raise ValueError("i doit être inférieur à j et j doit être inférieur à la longueur de la liste")
    

def TextToIndex(string):
    string = string.lower()
    liste = string.split()
    dico = {}
    for i in range(len(liste)):
        if liste[i] not in dico:
            dico[liste[i]] = [i]
        else:
            dico[liste[i]].append(i)
    return dico

def ListeEnDico(liste1, liste2):
    if len(liste1) != len(liste2):
        raise ValueError("Les deux listes doivent avoir la même longueur")
    else:
        dico = {}
        for i in range(len(liste1)):
            dico[liste1[i]] = liste2[i]
    return dico

def DicoEnListe(dico):
    liste1 = []
    liste2 = []
    for i in dico.keys():
        liste1.append(i)
        liste2.append(dico[i])
    return liste1, liste2

def ProtAmines(string, dico):
    #Ecrire une fonction qui reçoit une séquence de protéines et retourne la liste des acides aminés qui la composent
    listeAmines = []
    for i in range(len(string)):
        if string[i] in dico.keys():
            listeAmines.append(dico[string[i]])
    return listeAmines

def AminesProt(liste, dico):
    #Ecrire une fonction qui reçoit une liste d’acides aminés et retourne la séquence de protéines correspondante
    string = ""
    for i in range(len(liste)):
        for j in dico.keys():
            if liste[i] == dico[j]:
                string += j
    return string

# appel des foncions
#print("Rackam",rackam(Rackam1))
#print("Flavius", Flavius(41, 4))
#print("Hamming", Hamming("101010", "111010"))
#print("MemeVal", MemeVal([1, 2, 3, 4, 5, 4], [2, 4, 6, 8, 10, 4]))
#print("MemeVal2", MemeVal2("12345", "246810"))
#print("PermutListe", PermutListe([1, 2, 3, 4, 5], [2, 4, 1, 5, 3]))
#print("bookmaker", bookmaker(Dupont))
#print(CaracSolitaire("aasrffzrrrzzdttl"))
#print(GrandeSequence([1,8,-9,45,-75,3,9,-1,5,-9,4,-7,4,8,17,25,87,-4]))
#print(TextToIndex("Ceci est un texte. Un exemple de texte."))
#print(ListeEnDico(Code1L, Code3L))
#print(ProtAmines("CDEIKLMNPQR", ListeEnDico(Code1L, Code3L)))

