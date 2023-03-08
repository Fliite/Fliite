from random import randint

def dicoChffreLettre(n):
    #creation d'un dictionnaire qui associe un int aléatoire à une lettre
    ChiffreLettre = {}
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while n > 0:
        n -= 1
        lalpha = randint(0,len(alphabet)-1)
        k = alphabet[lalpha]
        nbre = randint(-5,5)
        alphabet.remove(k)
        ChiffreLettre.update({k : nbre})
    return ChiffreLettre

def fusionDico(dico1, dico2):
    #fusionne deux dictionnaires quelconques
    dico = {}
    for i in dico1:
        dico.update({i : dico1[i]})
    for i in dico2:
        dico.update({i : dico2[i]})
    for lettre in dico.keys():
        if lettre in dico1 and lettre in dico2:
            dico[lettre] = dico1[lettre] + dico2[lettre]
            if dico[lettre] == 0:
                del dico[lettre]
    return dico

def main():
    n = int(input("quelle taille des deux listes ?"))
    dico1 = dicoChffreLettre(n)
    dico2 = dicoChffreLettre(n)
    print(dico1,'\t',dico2)
    print(fusionDico(dico1, dico2))

if __name__ == "__main__":
    main()