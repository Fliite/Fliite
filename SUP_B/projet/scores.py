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