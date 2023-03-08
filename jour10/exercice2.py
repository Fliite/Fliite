minuscule = 'abcdefghijklmnopqrstuvwxyz'
majuscule = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def DicoBijectif(a,b):
    dico = {}
    for i in range(len(a)):
        dico.update({a[i]:b[i]})
    return dico

print(DicoBijectif(minuscule,majuscule))
