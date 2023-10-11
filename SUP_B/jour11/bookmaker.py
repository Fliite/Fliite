Code1L = "ACDEFGHIKLMNPQRSTVWY"
Code3L = ["ALA" , "CYS" , "ASP" , "GLU" , "PHE" , "GLY" , "HIS" , "ILE" , "LYS" , "LEU" , "MET" , "ASN" , "PRO" ,
"GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"]
test = ["MET" , "ASN" , "PRO" ,"GLN" , "ARG" , "SER" , "THR" , "VAL" , "TRP" , "TYR"]


def codageDesProts():
    dico = {}
    for i in range(len(Code1L)):
        dico[Code1L[i]] = Code3L[i]
    return dico

def reverseCodageDesProts():
    dico = {}
    for i in range(len(Code1L)):
        dico[Code3L[i]] = Code1L[i]
    return dico

print("codage des ports :",codageDesProts(),"\n\n reverse codage des ports :",reverseCodageDesProts())
