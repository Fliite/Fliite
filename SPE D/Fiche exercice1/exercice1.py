a = [[ 50, 'n'], [ 20 , 'e'] , [ 30 , 's'] , [ 82 , 'e'] , [ 48 , 'n'] , [ 43 , 'o'] , [ 51 , 's'] , [ 18 , 'n'] , [ 46 , 'e']]
b = [[ 15 , 'n'], [ 20 , 'e'] , [ 30 , 's'] , [ 82 , 'e'] , [ 48 , 'n'] , [ 43 , 'o'] , [ 51 , 's'] , [ 18 , 'n'] , [ 46 , 'e']]
c = [[ 15 , 'n'], [ 25 , 'e'] , [ 30 , 's'] , [ 12 , 'e'] , [ 48 , 'n'] , [ 43 , 'o'] , [ 51 , 's'] , [ 18 , 'n'] , [ 21 , 'e' ]]

# 'n' = nord, 's' = sud, 'e' = est, 'o' = ouest
#on cherche à simplifier le parcours en supprimant les déplacements inutiles
#le resultat est donné dans une liste de listes

def exercice1(parcours):
    ParcourSimplifie = []
    x = 0
    y = 0
    for i in parcours:
        if i[1] == 'n':
            y += i[0]
        elif i[1] == 's':
            y -= i[0]
        elif i[1] == 'e':
            x += i[0]
        elif i[1] == 'o':
            x -= i[0]
    if y > 0:
        ParcourSimplifie.append([y, 'n'])
    else:
        ParcourSimplifie.append([y, 's'])
    if x > 0:
        ParcourSimplifie.append([x, 'e'])
    else:
        ParcourSimplifie.append([x, 'o'])
    return ParcourSimplifie

print('a simplifié', exercice1(a))
print('b simplifié', exercice1(b))
print('c simplifié', exercice1(c))