import random

# Définition des couleurs et des valeurs des cartes
couleurs = ['Rouge', 'Vert', 'Bleu', 'Jaune']
ValCarte = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'SensInterdit', 'Contresens', 'PlusDeux']

# Définition de la classe Carte
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

# Définition du paquet de cartes sous forme de dictionnaire
deck = [{'color': color, 'value': value} for color in couleurs for value in ValCarte]

# Mélanger le paquet de cartes
random.shuffle(deck)

# Définition de la classe Joueur
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck, num_cards=1):
        for _ in range(num_cards):
            self.hand.append(deck.pop(0))

    def play_card(self, card_index):
        return self.hand.pop(card_index)


# Distribution des cartes aux joueurs
for player in Joueurs:
    player.draw_card(deck, 7)

# Carte du dessus de la pile
CarteJouee = deck.pop(0)

# Début du jeu
JoueurActuel = 0
direction = 1
while True:
    print(f"C'est au tour de {Joueurs[JoueurActuel].name}.")
    print(f"Carte en jeu : {CarteJouee}")

    # Affichage de la main du joueur
    print("Votre main :")
    for i, card in enumerate(Joueurs[JoueurActuel].hand):
        print(f"{i+1}: {card['color']} {card['value']}")
    
    # Vérification si le joueur peut jouer une carte
    CarteJouables = [card for card in Joueurs[JoueurActuel].hand if card['color'] == CarteJouee['color'] or card['value'] == CarteJouee['value']]
    if len(CarteJouables) > 0:
        choice = int(input("Choisissez le numéro de la carte à jouer (0 pour piocher) : "))
        if choice == 0:
            Joueurs[JoueurActuel].draw_card(deck)
        else:
            carteChoisie = Joueurs[JoueurActuel].play_card(choice - 1)
            CarteJouee = carteChoisie
            print(f"{Joueurs[JoueurActuel].name} a joué {carteChoisie['color']} {carteChoisie['value']}.")
            if len(Joueurs[JoueurActuel].hand) == 0:
                print(f"{Joueurs[JoueurActuel].name} a gagné!")
                break
            if carteChoisie['value'] == 'Reverse':
                direction *= -1
            elif carteChoisie['value'] == 'Skip':
                JoueurActuel += direction
            elif carteChoisie['value'] == 'Draw Two':
                next_player = (JoueurActuel + direction) % len(Joueurs)
                Joueurs[next_player].draw_card(deck, 2)
    else:
        print("Aucune carte jouable. Piochez une carte.")
        Joueurs[JoueurActuel].draw_card(deck)

    JoueurActuel = (JoueurActuel + direction) % len(Joueurs)

def initialisation():
    # Initialisation des joueurs
    NbreJoueurs = int(input("Entrez le nombre de joueurs : "))
    Joueurs = [Player(input(f"Entrez le nom du joueur {i+1}: ")) for i in range(NbreJoueurs)]
    
    return Joueurs

def Tour(Joueurs): # la variqble Joueurs est une liste de joueurs
    JoueurActuel = 0
    direction = 1
    print(f"C'est au tour de {Joueurs[JoueurActuel].name}.") # Chaque joueur a un numéro attribué. La fonction .name permet d'afficher le nom du joueur
    print(f"Carte en jeu : {CarteJouee}")
    # Affichage de la main du joueur
    print("Votre main :")
    for i, card in enumerate(Joueurs[JoueurActuel].hand): # print le deck du joueur actuel
        print(f"{i+1}: {card['color']} {card['value']}")

def Verifier(CarteJouee, deck): #retourne une liste de cartes jouables (ou none si aucune carte n'est jouable)
    return cartes

def Veifier2(): #retourne False si la carte ne peut pas être jouée, True si elle peut être jouée
    return cartes    
def main():
    initialisation()
    while True:
        Tour()
    
if __name__ == "__main__":
    main()