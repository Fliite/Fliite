#creer morpion 3x3

plateau = [["A1", "A2", "A3"], ["B1", "B2", "B3"], ["C1", "C2", "C3"]]

def show_board(plateau):
    for i in range(len(plateau)):
        print(plateau[i])

show_board(plateau)