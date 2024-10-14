import tkinter as tk
import random

# Créer la fenêtre principale
window = tk.Tk()
window.title("Exemple de Canvas")
window.geometry("600x600")  # Définir la taille de la fenêtre à 600x600 pixels
window.resizable(False, False)  # Désactiver le redimensionnement de la fenêtre

# Créer la fenetre
canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

# Ajoutez votre code pour dessiner sur le canvas ici

def draw_rectangles(n, x, y, canvas, ecart):
    if n <= 0:
        return
    canvas.create_rectangle(x, y, x + 50, y + 50, fill="blue")  # Example rectangle dimensions
    canvas.create_rectangle(x, y + 50 + ecart, x + 50, y + 100 + ecart, fill="red")  # Red rectangle dimensions
    canvas.create_rectangle(x, y + 100 + ecart * 2, x + 50, y + 150 + ecart * 2, fill="green")  # Green rectangle dimensions
    draw_rectangles(n - 1, x + 50 + ecart, y, canvas, ecart)  # Recursive call with updated coordinates

draw_rectangles(5, 0, 0, canvas, 10)  # Example usage with 5 rectangles separated by 10 pixels

cartes = [1,2,3,4,5,6,7,8,9, 'sensInterdit', 'contresens', '+2']
couleurs = ['rouge', 'bleu', 'vert', 'jaune']


def distribution(nbre_joueurs):
    joueurs = {}  # Create an empty dictionary to store the players
    for i in range(nbre_joueurs):
        joueurs[i+1] = {}  # Assign an empty dictionary to each player
        for _ in range(7):
            couleur = random.choice(couleurs)  # Choose a random color from the list
            valeur = random.choice(cartes)  # Choose a random value from the list
            joueurs[i+1][couleur] = valeur  # Assign the value to the corresponding color key
    return joueurs