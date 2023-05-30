import tkinter as tk
import json

def sauvegarder_scores(scores):
    with open("scores.json", "w") as fichier:
        json.dump(scores, fichier)

def charger_scores():
    try:
        with open("scores.json", "r") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return {}

def ajouter_score(scores, joueur, score):
    if joueur in scores:
        scores[joueur] += score
    else:
        scores[joueur] = score

def afficher_scores(scores):
    for joueur, score in scores.items():
        print(joueur, ":", score)

def enregistrer_scores():
    sauvegarder_scores(scores)
    print("Scores enregistrés.")

def ajouter_joueur():
    joueur = entree_nom.get()
    score = int(entree_score.get())

    ajouter_score(scores, joueur, score)

    entree_nom.delete(0, tk.END)
    entree_score.delete(0, tk.END)

    afficher_scores(scores)

def quitter():
    fenetre.destroy()

fenetre = tk.Tk()
fenetre.title("Menu des scores")

# Chargement des scores existants
scores = charger_scores()

# Création des widgets
label_nom = tk.Label(fenetre, text="Nom du joueur :")
label_score = tk.Label(fenetre, text="Score du joueur :")
entree_nom = tk.Entry(fenetre)
entree_score = tk.Entry(fenetre)
bouton_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_joueur)
bouton_enregistrer = tk.Button(fenetre, text="Enregistrer les scores", command=enregistrer_scores)
bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter)

# Placement des widgets dans la grille
label_nom.grid(row=0, column=0)
label_score.grid(row=1, column=0)
entree_nom.grid(row=0, column=1)
entree_score.grid(row=1, column=1)
bouton_ajouter.grid(row=2, column=0, columnspan=2, pady=10)
bouton_enregistrer.grid(row=3, column=0, columnspan=2, pady=10)
bouton_quitter.grid(row=4, column=0, columnspan=2)

# Affichage des scores existants
afficher_scores(scores)

# Démarrage de la boucle principale de l'application
fenetre.mainloop()
