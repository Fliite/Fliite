from random import randint

dico1 = {"Louis": 45, "Jean": 25, "Marie": 30, "Pierre": 20, "Paul": 35}
dico2 = {"banana": "banane", "apple": "pomme", "orange": "orange", "pear": "poire", "grape": "raisin"}

Majuscule = {"a" : "A", "b" : "B", "c" : "C", "d" : "D", "e" : "E", "f" : "F", "g" : "G", "h" : "H", "i" : "I", "j" : "J", "k" : "K", "l" : "L", "m" : "M", "n" : "N", "o" : "O", "p" : "P", "q" : "Q", "r" : "R", "s" : "S", "t" : "T", "u" : "U", "v" : "V", "w" : "W", "x" : "X", "y" : "Y", "z" : "Z"}
Minuscule = {"A" : "a", "B" : "b", "C" : "c", "D" : "d", "E" : "e", "F" : "f", "G" : "g", "H" : "h", "I" : "i", "J" : "j", "K" : "k", "L" : "l", "M" : "m", "N" : "n", "O" : "o", "P" : "p", "Q" : "q", "R" : "r", "S" : "s", "T" : "t", "U" : "u", "V" : "v", "W" : "w", "X" : "x", "Y" : "y", "Z" : "z"}

def FrançaisCharabia():
    #retourne un dictionnaire de traduction français-charabia
    #on mixe les lettres de l'alphabet
    Français_Charabia = {}
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alphabe = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(26):
        l = randint(0,len(alphabet)-1)
        k = alphabet[l]
        alphabet.remove(k)
        Français_Charabia.update({alphabe[i] : k})
    return Français_Charabia

def mot():
    mot = input("Entrez un mot : ")
    return mot

def minuscule(stringg, Minuscule):
    #retourne une chaine de caractères en minuscule à partir du dictionnaire
    for i in stringg:
        if i in Minuscule:
            stringg = stringg.replace(i, Minuscule[i])
    return stringg

def majuscule(stringg, Majuscule):
    #retourne une chaine de caractères en majuscule à partir du dictionnaire
    for i in stringg:
        if i in Majuscule:
            stringg = stringg.replace(i, Majuscule[i])
    return stringg
        
def françaisEnCharabia(mot, Français_Charabia):
    #retourne un mot en charabia à partir du dictionnaire
    for i in mot:
        if i in Français_Charabia:
            mot = mot.replace(i, Français_Charabia[i])
    return mot

def charabiaEnFrançais(mot, Français_Charabia):
    #retourne un mot en français à partir du dictionnaire
    for i in mot:
        for k in Français_Charabia:
            if i == Français_Charabia[k]:
                mot = mot.replace(i, k)
    return mot

#retourne un mot en charabia quel qu'il soit
def main():
    WORD = mot()
    word = minuscule(WORD, Minuscule)
    dico = FrançaisCharabia()
    charab = françaisEnCharabia(word, dico)
    print("Le mot", WORD, "en charabia est", charab)

main()
