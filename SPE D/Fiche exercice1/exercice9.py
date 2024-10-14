text1 = "Ceci est un texte. Un exemple de texte."

def decompo_en_liste(texte):
    #on prend en entree une pharse ponctuee et en sortie une liste de mots du texte dans l'ordre
    #on enleve la ponctuation, on met en minuscule et on separe les mots
    texte = texte.replace('.', '')
    texte = texte.replace(',', '')
    texte = texte.lower()
    text = texte.split() #permet de mettre en liste la phrase
    return text

liste = decompo_en_liste(text1)

def mise_en_dico(liste):
    #on prend en entree une liste de mots et en sortie un dictionnaire avec les mots comme cle et une liste de leur position comme valeur
    dico = {}
    k = 0
    for i in liste:
        if i not in dico:
            dico[i] = [k]
        else:
            dico[i].append(k)
        k += 1
    return dico

print(mise_en_dico(liste))