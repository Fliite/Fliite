import random

cartes = [1,2,3,4,5,6,7,8,9, 'sensInterdit', 'contresens', '+2']
couleurs = ['rouge', 'bleu', 'vert', 'jaune']

def distribution(nbre_joueurs):
    joueurs = {}  # Create an empty dictionary to store the players
    for i in range(nbre_joueurs):
        joueurs[i+1] = {}  # Assign an empty dictionary to each player
        m = 0
        for m in range(7):
            m += 1
            couleur = random.choice(couleurs)  # Choose a random color from the list
            valeur = random.choice(cartes)  # Choose a random value from the list
            joueurs[i+1][couleur] = valeur  # Assign the value to the corresponding color key
    return joueurs

print(distribution(1))  # Example usage with 4 players