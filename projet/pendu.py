import random
import time

def lire_dictionnaire(): #fonction qui lit le dictionnaire et le met dans une grande liste
    mots = [] 
    with open("projet/aa.txt", "r") as fichier: #ouvre le fichier en mode lecture
        mots = fichier.read().splitlines() #splitlines() permet de séparer les mots en les mettant dans une liste
    return mots

def choisir_mot(mots):
    return random.choice(mots)

def afficher_mot_cache(mot, lettres_trouvees): #fonction qui affiche le mot avec les lettres trouvées
    mot_cache = ""
    for lettre in mot: #on compose le mot à afficher lettre par lettre 
        if lettre in lettres_trouvees: #cela permet de mettre une lettre plusieurs fois si elle est dans le mot
            mot_cache += lettre
        else:
            mot_cache += "_" #permet au joueur de savoir où les lettres manquent
    return mot_cache

def afficher_lettres_fausses(lettres_fausses): #fonction qui affiche les lettres fausses
    print("Lettres fausses :")
    for lettre in lettres_fausses:
        print(lettre, end=" ") #end=" " permet de ne pas faire de retour à la ligne
    print("\n") 

def deviner_mot(mot): #boucle principale du jeu
    lettres_trouvees = [] #permet de stocker les lettres trouvées pour les afficher ensuite
    lettres_fausses = [] #permet de stocker les lettres fausses pour les afficher ensuite
    tentatives_restantes = 8

    while tentatives_restantes > 0:     
        print("Mot à deviner :", afficher_mot_cache(mot, lettres_trouvees))
        afficher_lettres_fausses(lettres_fausses)
        print("Tentatives restantes :", tentatives_restantes)

        lettre = input("Entrez une lettre : ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre.")
            pass #permet de revenir au début de la boucle

        elif lettre in lettres_trouvees or lettre in lettres_fausses:
            print("Lettre déjà essayée.")
            pass

        elif lettre in mot: #condition gagnante
            lettres_trouvees.append(lettre)
            if mot == afficher_mot_cache(mot, lettres_trouvees):
                print("Bravo ! Vous avez deviné le mot :", mot)
                return True #permet de sortir de la boucle et de savoir si le joueur a gagné
        else: #condition perdante
            lettres_fausses.append(lettre)
            tentatives_restantes -= 1

    print("Désolé, vous avez épuisé toutes vos tentatives.")
    print("Le mot à deviner était :", mot)
    return False

def main():
    mots = lire_dictionnaire()
    mot = choisir_mot(mots)
    print("Bienvenue dans le jeu du pendu !")
    print("Vous avez 8 tentatives pour deviner le mot.")

    debut = time.time() #chronomètre le temps que le boucle deviner_mot prend
    victoire = deviner_mot(mot)
    fin = time.time()

    if victoire: #ssi le joueur a gagné
        temps = fin - debut
        minutes = int(temps / 60)
        secondes = int(temps % 60)
        print("Vous avez deviné le mot en", minutes, "minutes et", secondes, "secondes.")

if __name__ == "__main__": 
    main()