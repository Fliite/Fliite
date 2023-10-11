#create random list of names
#a name is composed of one vowel for every two consonants

def main():
    liste = prenoms_hasard(10)
    print(liste)



from random import randint

def liste_hasard(length, start, rangee):
    liste = []
    i = 0
    while i < length:
        i += 1
        ha = randint(start, rangee - start)
        liste.append(ha)
    return liste


def prenoms_hasard(length):
    liste = []
    i = 0
    while i < length:
        i += 1
        pren = prenom_random()
        liste.append(pren)
    return liste

def prenom_random():
    voyelles = ['b','c','d','f','g','h','j','k','l','m','n','p','r','s','t']
    consonnes = ['a','e','i','o','u']
    lettres_prenom = randint(2, 5)
    prenom = []
    i = 0
    while i < lettres_prenom: 
        i += 1
        vr = randint(0, len(voyelles)-1)
        vc = randint(0, len(consonnes)-1)
        prenom.append(voyelles[vr])
        prenom.append(consonnes[vc])
    pren =''.join(str(e) for e in prenom)
    return pren


if __name__ == '__main__':
    main()