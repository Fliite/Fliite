#creer morpion 3x3

plateau = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]

def show_board(plateau):
    for i in range(len(plateau)):
        print("\n")
        for j in range(len(plateau[i])):
            print(plateau[i][j], end=" ")
    print("\n")

def checkwin(plateau):
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == plateau[i][j+1]:
                print("Le joueur", plateau[i][j], "a gagné !")
                exit()
            elif plateau[j][i] == plateau[j+1][i]:
                print("Le joueur", plateau[j][i], "a gagné !")
                exit()

class joueur:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
        def play(self, plateau):
            print("C'est au tour de", self.name)
            print("Quelle case voulez-vous jouer ?")
            case = input()
            for i in range(len(plateau)):
                for j in range(len(plateau[i])):
                    if plateau[i][j] == case:
                        plateau[i][j] = self.symbol
                        return plateau
            print("Cette case n'existe pas !")
            return plateau