import random

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

def initialiser_paquet():
    couleurs = ['rouge', 'bleu', 'vert', 'jaune']
    valeurs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'sens interdit', 'Contresens', '+2']
    paquet = []
    for valeur in valeurs:
        for couleur in couleurs:
            paquet.append(Carte(couleur, valeur))
            if valeur != '0':
                paquet.append(Carte(couleur, valeur))  # Ajoute deux fois chaque carte sauf '0'
    for _ in range(4):
        paquet.append(Carte(None, '+4'))  # Ajoute 4 cartes +4
        paquet.append(Carte(None, 'Joker'))  # Ajoute 4 cartes joker
    random.shuffle(paquet)
    return paquet

def distribuer_cartes(joueurs, paquet):
    for _ in range(7):
        for joueur in joueurs:
            joueur.piocher_carte(paquet.pop())

def montrer_main(joueur):
    print(f"Main de {joueur.nom}:")
    for i, carte in enumerate(joueur.main):
        print(f"{i+1}: {carte.couleur} {carte.valeur}")

def jouer_tour(joueur_actuel, carte_superieure, sens, paquet, joueurs):
    print(f"C'est au tour de {joueur_actuel.nom}.")
    print(f"Carte en jeu : {carte_superieure.couleur} {carte_superieure.valeur}")
    montrer_main(joueur_actuel)
    cartes_jouables = []
    for carte in joueur_actuel.main:
        if carte.couleur == carte_superieure.couleur or carte.valeur == carte_superieure.valeur or carte_superieure.couleur is None:
            cartes_jouables.append(carte)
    if cartes_jouables:
        choix = int(input("Choisissez le numéro de la carte à jouer : ")) - 1
        while choix < 0 or choix >= len(cartes_jouables):
            choix = int(input("Choix invalide. Choisissez le numéro de la carte à jouer : ")) - 1
        carte_jouee_index = joueur_actuel.main.index(cartes_jouables[choix])
        carte_jouee = joueur_actuel.jouer_carte(carte_jouee_index)
        if carte_jouee.valeur == '+4':
            carte_superieure = plus_quatre(joueurs, joueur_actuel, paquet)
        elif carte_jouee.valeur == 'sens interdit':
            changer_sens(sens)
        elif carte_jouee.valeur == 'Contresens':
            inverser_ordre(joueurs, sens)
        elif carte_jouee.valeur == 'Joker':
            nouvelle_couleur = choisir_couleur()
            carte_jouee.couleur = nouvelle_couleur
            carte_superieure = carte_jouee
        else:
            carte_superieure = carte_jouee
    else:
        joueur_actuel.piocher_carte(paquet.pop())
    return carte_superieure

def plus_quatre(joueurs, joueur_actuel, paquet):
    nouvelle_couleur = choisir_couleur()
    joueur_suivant = (joueurs.index(joueur_actuel) + 1) % len(joueurs)
    for _ in range(4):
        joueurs[joueur_suivant].piocher_carte(paquet.pop())
    print(f"{joueurs[joueur_suivant].nom} doit piocher 4 cartes et la couleur devient {nouvelle_couleur}.")
    return Carte(nouvelle_couleur, '00')

def choisir_couleur():
    couleurs = ['rouge', 'bleu', 'vert', 'jaune']
    choix = int(input("Choisissez une nouvelle couleur : "))
    while choix < 1 or choix > 4:
        choix = int(input("Choix invalide. Choisissez une nouvelle couleur : "))
    return couleurs[choix - 1]

def changer_sens(sens):
    sens *= -1
    print("Le sens de jeu a été inversé.")

def inverser_ordre(joueurs, sens):
    sens *= -1
    joueurs.reverse()
    print("L'ordre des joueurs a été inversé.")

def verifier_victoire(joueurs):
    for joueur in joueurs:
        if not joueur.main:
            return joueur.nom
    return None

def Programme_principal():
    nombre_joueurs = int(input("Entrez le nombre de joueurs : "))
    joueurs = []
    for i in range(nombre_joueurs):
        nom_joueur = input(f"Entrez le nom du joueur {i+1}: ")
        joueur = Joueur(nom_joueur)
        joueurs.append(joueur)
    paquet = initialiser_paquet()
    distribuer_cartes(joueurs, paquet)
    carte_superieure = paquet.pop()

    sens = 1  # Sens de jeu (1 pour avant, -1 pour arrière)

    while True:
        for joueur in joueurs[::sens]:  # Parcours des joueurs dans le sens
            carte_superieure = jouer_tour(joueur, carte_superieure, sens, paquet, joueurs)
            if not joueur.main:  # Si le joueur a joué toutes ses cartes
                print(f"{joueur.nom} a gagné !")
                return

if __name__ == "__main__":
    Programme_principal()
