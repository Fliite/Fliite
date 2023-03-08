Dupont = { (10,6) : -25.0 , (15,6) : -5.0 , (22,6) : -35.0 , (30,6) : 93.50 , (4,7) : -10.0 , (8,7) : -10.0 , (15,7) : -5.0 }

def dates():
    lesDates =[i for i in Dupont.keys()]
    lesSommes = [i for i in Dupont.values()]
    somme = [sum(lesSommes[:i+1]) for i in range(len(lesSommes))]
    endvalue = somme[-1]

    return lesDates, lesSommes, somme, endvalue

print(dates())