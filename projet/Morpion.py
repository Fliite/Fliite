#jeu de morpion sans tkinter
#Deux plateaux  sont en parallèle
#le jeu se passe sur le plateau vide
#le plateau plein sert à afficher les coups joués


def plateau_vide(size):
    plateau = []
    for i in range(size): #permet de créer les lignes
        plateau.append([])
        for j in range(size): #permet de créer les colonnes
            plateau[i].append(" ")
    return plateau

def plateau_plein(size): 
    #on construit un plateau carre de taille size
    #on replit le plateau avec le nom des cases (A1, A2, A3, B1, B2, B3, C1, C2, C3 etc)
    #l'affaichage s'adaptera à la taille du plateau
    plateau = plateau_vide(size)
    for i in range(size):
        lettre = chr(65 + i)
        for j in range(size):
            plateau[i][j] = str(lettre) + str(j)
    return plateau

def jouer1(plateau, size):
    #le joueur 1 joue
    while 


def afficher_plateau(plateau):
    for i in range(len(plateau)):
        print(plateau[i])

def checkwin(plateau, size):
    #verifie si un joueur a gagné
    #il faut que les size cases soient identiques(diagonales, lignes, colonnes)
    
    #diagonales
    for i in range(size-1):
        if plateau[i][i] == plateau[i+1][i+1]:
            print("Le joueur", plateau[i][i], "a gagné !")
            exit()
        elif plateau[i][size-i] == plateau[i+1][size-i-1]:
            print("Le joueur", plateau[i][size-i], "a gagné !")
            exit()
    #lignes
    for i in range(size):
        for j in range(size):
            if plateau[i][j] == plateau[i][j+1]:
                print("Le joueur", plateau[i][j], "a gagné !")
                exit()
    #colonnes
    for i in range(size):
        for j in range(size):
            if plateau[j][i] == plateau[j+1][i]:
                print("Le joueur", plateau[j][i], "a gagné !")
                exit()

def main():
    size = 3
    plein = plateau_plein(size)
    afficher_plateau(plein)
    jouer1(plein, size)

if __name__ == "__main__":
    main()