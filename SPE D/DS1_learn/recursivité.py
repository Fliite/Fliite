def trouver(pL):
    if 1 in pL:
        return pL.index(1)
    return -1

def propage(pL, pVal):
    i = trouver(pL)
    if i == -1 :
        return
    pL[i] = pVal
    if (len(pL)-i) > 1:
        if pL[i+1] == 1:
            propage(pL, pVal)
        else:
            propage(pL, pVal+1)

maListe = [0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0]
propage(maListe, 2)
print(maListe)
