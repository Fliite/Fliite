dico={'A':-5 , 'C':10 , 'Z':-3 , 'T':4, 'M':2 , 'E':1}

def retourne_cle_val():
    cle = [i for i in dico.keys()]
    val = [i for i in dico.values()]
    return cle, val