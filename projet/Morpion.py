#jeu de morpion sans tkinter
#Deux plateaux  sont en parallèle
#le jeu se passe sur le plateau vide
#le plateau plein sert à afficher les coups joués


def plateau_plein(size):
    plateau = []
    for i in range(size):
        lettre = chr(65 + i) #les letttres correspondent aux lignes
        plateau.append([])
        for j in range(size):
            plateau[i].append(str(lettre) + str(j + 1))  # Ajouter +1 pour les numéros de colonne
    return plateau

def afficher_plateau(plateau):
    for i in range(len(plateau)):
        print('\n')
        for j in range(len(plateau[i])):
            print(plateau[i][j], end=" ")

afficher_plateau(plateau_plein(3))

def a_gagné(gagnant): #permet d'associer un nom de joueur à un symbole
    print("Le joueur", gagnant, "a gagné !")


def checkwin(plateau, size):
    # Vérifie si un joueur a gagné
    # Il faut que les "size" cases soient identiques (diagonales, lignes, colonnes)

    # Diagonales
    for i in range(size-1): # (size-1) pour ne pas déborder du tableau
        if plateau[i][i] == plateau[i+1][i+1]: #diag 1
            gagnant = plateau[i][i]
            a_gagné(gagnant)
            exit()
        elif plateau[i][size-i-1] == plateau[i+1][size-i-2]:  # Modifier size-i en size-i-1 et ajouter size-i-2
            gagnant = plateau[i][size-i-1]
            a_gagné(gagnant)
            exit()

    # Lignes
    for i in range(size):
        for j in range(size-1):  # Modifier size-1 pour éviter un débordement de tableau
            if plateau[i][j] == plateau[i][j+1]:
                gagnant = plateau[i][j]
                a_gagné(gagnant)
                exit()

    # Colonnes
    for i in range(size):
        for j in range(size-1):  # Modifier size-1 pour éviter un débordement de tableau
            if plateau[j][i] == plateau[j+1][i]:
                gagnant = plateau[j][i]
                a_gagné(gagnant)
                exit()

def tour(plateau):
    