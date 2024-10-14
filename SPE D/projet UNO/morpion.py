def print_plateau(plateau): #affiche le plateau de jeu
    print("   1  2  3")
    for i in range(3):
        row = f"{chr(ord('A') + i)}  " #f : retour à la ligne et chr() renvoie le caractere correspondant au code ASCII
        for j in range(3): #chr(ord('A') + i) : A, B, C pour range(3)
            row += f"{plateau[i][j]}  " #plateau[i][j] : case du tableau ## ajoute un espace
        print(row)

def Jouer_coup(player): #demande au joueur de choisir une case, verifie que le choix est valide
    while True:
        move = input(f"Joueur {player}, jouez un coup: ")
        if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
            print("Cette case n'existe pas.") 
        else:
            row = ord(move[0]) - ord('A') #ord() renvoie le code ASCII d'un caractere
            col = int(move[1]) - 1
            return row, col

def check_win(plateau): #verifie si un joueur a gagné
    for i in range(3): #verifie les lignes et les colonnes
        if plateau[i][0] == plateau[i][1] == plateau[i][2] != " ":
            return plateau[i][0]
        if plateau[0][i] == plateau[1][i] == plateau[2][i] != " ":
            return plateau[0][i]
    if plateau[0][0] == plateau[1][1] == plateau[2][2] != " ": #diagonale1
        return plateau[0][0]
    if plateau[0][2] == plateau[1][1] == plateau[2][0] != " ": #diagonale2
        return plateau[0][2]
    return None

def jouer(): #fonction principale, lance le jeu
    plateau = [[" "]*3 for i in range(3)] #crée un tableau de 3x3
    player = "X"
    score = {"X": 0, "O": 0} #score interne à la partie
    while True: #boucle principale
        print_plateau(plateau)
        row, col = Jouer_coup(player)
        if plateau[row][col] != " ":
            print("La case est déja occupée.")
            continue 
        plateau[row][col] = player
        winner = check_win(plateau)
        if winner is not None: #si un joueur a gagné, affiche le plateau de jeu, le gagnant et le score
            print_plateau(plateau)
            print(f"Le joueur {winner} a gagné!")
            score[winner] += 1
            print(f"Score: joueur X: {score['X']} - joueur O: {score['O']}")
            return
        if all(plateau[i][j] != " " for i in range(3) for j in range(3)): #all() renvoie True si tous les elements d'une liste sont True
            #si toutes les cases sont remplies et qu'il n'y a pas de gagnant, match nul
            print_plateau(plateau)
            print("Match NUL!")
            score["X"] += 0.5
            score["O"] += 0.5
            print(f"Score: X: {score['X']} - O: {score['O']}")
            return
        player = "O" if player == "X" else "X"

jouer()