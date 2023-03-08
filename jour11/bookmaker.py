Code1L = "ACDEFGHIKLMNPQRSTVWY"
Code3L = ["ALA" , "CYS" , "ASP" , "GLU" , "PHE" , "GLY" , "HIS" , "ILE" , "LYS" , "LEU" , "MET" , "ASN" , "PRO" ,
"GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"]
test = ["MET" , "ASN" , "PRO" ,"GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"]


def codageDesProts(Code1L, Code3L):
    dico = {}
    for i in range(len(Code1L)):
        dico[Code1L[i]] = Code3L[i]
    return dico

def reverseCodageDesProts(Code1L, Code3L):
    dico = {}
    for i in range(len(Code1L)):
        dico[Code3L[i]] = Code1L[i]
    return dico

def retourne1L(test, dico):
    prot1L = ""
    for i in test:
        prot1L += dico[i]
    return prot1L

retourne1L(test, reverseCodageDesProts(Code1L, Code3L))
