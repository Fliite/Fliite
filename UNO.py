import random
from time import sleep

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def piocher_carte(self, carte):
        self.main.append(carte)

    def jouer_carte(self, index):
        return self.main.pop(index)

def initialiser_paquet(): # Créer un paquet de cartes mélangé
    couleurs = ['rouge', 'bleu', 'vert', 'jaune']
    valeurs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sens interdit', 'Contresens', '+2']
    paquet = [Carte(couleur, valeur) for couleur in couleurs for valeur in valeurs]
    random.shuffle(paquet)
    return paquet

def distribuer_cartes(joueurs, paquet):
    for i in range(7):
        for joueur in joueurs:
            joueur.piocher_carte(paquet.pop())

def montrer_main(joueur):
    print(f"Main de {joueur.nom}:")
    for i, carte in enumerate(joueur.main):
        print(f"{i+1}: {carte.couleur} {carte.valeur}")

def jouer_tour(joueur_actuel, carte_superieure):
    print(f"C'est au tour de {joueur_actuel.nom}.") # le f permet d'insérer des variables dans une chaîne de caractères
    sleep(3) # On ne triche pas en regardant les cartes des autres joueurs
    print(f"Carte en jeu : {carte_superieure.couleur} {carte_superieure.valeur}")
    montrer_main(joueur_actuel)
    cartes_jouables = []
    for carte in joueur_actuel.main:
        if carte.couleur == carte_superieure.couleur or carte.valeur == carte_superieure.valeur:
            cartes_jouables.append(carte)
    if cartes_jouables: # Si le joueur a au moins une carte jouable
        choix = int(input("Choisissez le numéro de la carte à jouer : ")) - 1 # Le -1 est pour correspondre à l'index de la liste (la première carte est à l'index 0)
        while choix < 0 or choix >= len(cartes_jouables): # Vérifier si le choix est valide
            choix = int(input("Choix invalide. Choisissez le numéro de la carte à jouer : ")) - 1
        return joueur_actuel.jouer_carte(joueur_actuel.main.index(cartes_jouables[choix]))
    else: # la règle est de piocher une carte si le joueur n'a pas de carte jouable
        print("Aucune carte jouable. Piochez une carte.")
        return None

def verifier_victoire(joueurs):
    for joueur in joueurs:
        if not joueur.main:
            return joueur.nom
    return None

def principal():
    nombre_joueurs = int(input("Entrez le nombre de joueurs : "))
    joueurs = [Joueur(input(f"Entrez le nom du joueur {i+1}: ")) for i in range(nombre_joueurs)]
    paquet = initialiser_paquet()
    distribuer_cartes(joueurs, paquet)
    carte_superieure = paquet.pop() # La première carte du paquet est la carte supérieure

    while True:
        for joueur in joueurs:
            carte_jouee = jouer_tour(joueur, carte_superieure)
            if carte_jouee: 
                carte_superieure = carte_jouee # La carte jouée devient la carte supérieure
            else:
                joueur.piocher_carte(paquet.pop()) # .pop() retire le dernier élément de la liste

            gagnant = verifier_victoire(joueurs)
            if gagnant: # condition implicite : if gagnant is not None
                print(f"{gagnant} a gagné !")
                return

if __name__ == "__main__":
    principal()
