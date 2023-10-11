def isole_les_medocs(stock):
    names = []
    for i in range(len(stock)):
        names.append(stock[i][0])
    return names


def ajoutmedoc(stock, ajout):
    leng = len(stock)
    for i in range(leng):
        if stock[i][0] == ajout:
            stock [i][1] += 1
            break
        elif i == leng - 1:
            stock.append([ajout, 1, 0])
    return stock

def vendremedoc(stock, vendre):
    for i in range(len(stock)):
        if stock[i][0] == vendre:
            stock [i][1] -= 1
            if stock [i][1] == 0:
                del stock[i]
            break
    return stock

def prix(stock):
    lens = len(stock)
    for i in range(lens):
        print('\n le prix de', stock[i][0], 'est', stock[i][2])
        stock[i][2] = int(input('taper le nouveau prix: '))
        while stock[i][2] < 0:
            print('le prix doit etre positif')
            stock[i][2] = int(input('taper le nouveau prix: '))
    return stock

def changer_le_stock(stock):
    lens = len(stock)
    for i in range(lens):
        print('\n la quantité de', stock[i][0], 'est', stock[i][1])
        stock[i][1] = int(input('taper la nouvelle quantité: '))
        while stock[i][1] < 0:
            print('la quantité doit etre positive ou nulle')
            stock[i][1] = int(input('taper la nouvelle quantité: '))
    return stock


def argent_total(stock):
    total = 0
    for i in range(len(stock)):
        total += stock[i][1] * stock[i][2]
    return total