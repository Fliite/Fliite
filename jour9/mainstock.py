from medocs import *

#faut retravailler le main

def choix():
    stock = [['benadryl',5,15],['xumex',3,34],['ritalin',3,25]]
    choix = -1
    while choix < 0 or choix > 6:
        choix = int(input('taper \n 1 pour ajouter un nouveau médicament, \n 2 pour vendre un médicament, \n 3 pour changer le prix des médicaments, \n 4 pour changer le stock des médicaments, \n 5 pour afficher le prix total du stock \n'))
    if choix == 1:
        ajout = input('taper le nom du médicament à ajouter: ')
        ajoutmedoc(stock, ajout)
    elif choix == 2:
        vendre = input('taper le nom du médicament à vendre: ')
        vendremedoc(stock, vendre)
    elif choix == 3:
        prix(stock)
    elif choix == 4:
        changer_le_stock(stock)
    elif choix == 5:
        print('le prix total du stock est de', argent_total(stock), 'euros')

def main():
    stock = [['benadryl',5,15],['xumex',3,34],['ritalin',3,25]]
    changer_le_stock(stock)
    prix(stock)
    print('le stock final est', isole_les_medocs(stock), "d'une valeur totale de", argent_total(stock),"euros")
    print(stock)
    return stock

if __name__ == '__main__':
    choix()
