Code1L = "ACDEFGHIKLMNPQRSTVWY"
Code3L = ["ALA" , "CYS" , "ASP" , "GLU" , "PHE" , "GLY" , "HIS" , "ILE" , "LYS" , "LEU" , "MET" , "ASN", "PRO" , "GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"]

def asso(liste1, liste2):
    dico1 = {}
    for i in range(len(liste1)):
        dico1[liste1[i]] = liste2[i]
    return dico1

########TEMP
sequence = 'AKCD'
dico = asso(Code1L, Code3L)
####


def Sequenceprotéique(dictionnaire, string):
    #on associe lettres de asso avec la cle du dico
    h = []
    for i in sequence:
        if i not in dico:
            raise ValueError("La séquence ne correspond pas au code")
        else:
            #on ajoute la valeur de l'item de rang i à la liste h
            h.append(dico[i])
    return h

print(Sequenceprotéique(dico, sequence))