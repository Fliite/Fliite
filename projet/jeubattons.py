from random import randint
from time import sleep

#fonction qui fait jouer un 2 eme joueur ou un bot
def player2(bot, nbatons):
    #le bot joue si bot == True
    if bot == True: 
        sleep(1)
        a = (nbatons-1)%4 ### CONDITION SPECIFIQUE
        #une fois dans cette boucle, le bot gagne
        if a != 0:
            pl2 = a
            sleep(2)
            print("Le bot a retiré", pl2, "batons")
        #si il ne peut pas gagner, il retire 1 baton par défaut
        else:
            pl2 = 1
            sleep(2)
            print("Le bot a retiré", pl2, "batons")
    #autrement, l'autre joueur joue
    elif bot == False:
        pl2 = int(input("Joueur 2 : combien de batons voulez-vous retirer ? "))
    return pl2

#c'est la trame pour chaque tour
def trame(nbatons, bot):
    #la condition se reperte tant qu'il reste plus d'un baton
    #si il ne reste qu'un baton, le joueur qui joue perd
    while nbatons > 1:
        pl1 = 0
        pl2 = 0

        #condition qui vérifie que le joueur ne retire qu'entre 1 et 3 batons
        #joueur 1
        while pl1 < 1 or pl1 > 3: 
            pl1 = int(input("Joueur 1 : combien de batons voulez-vous retirer ? "))
        nbatons = nbatons - pl1
        checkwin(nbatons)

        print("Il reste", nbatons, "batons. \n")
        print("c'est au tour du joueur 2.")
        
        #condition qui vérifie que le joueur 2 ne retire qu'entre 1 et 3 batons
        #joueur 2
        while pl2 < 1 or pl2 > 3:
            pl2 = player2(bot, nbatons)
        nbatons = nbatons - pl2
        checkwin(nbatons)

        print("Il reste", nbatons, "batons. \n")
        print("c'est au tour du joueur 1.")

#fonction pour vérifier si le dernier joueur a perdu
def checkwin(nbatons):
    if nbatons <= 1:
        print("Il reste", nbatons, "batons. \n")
        print("Vous avez perdu")
        exit()

#fonction pour expliquer le jeu au départ
def notice():
    print("Le but est de ne pas retirer le dernier baton. \nVous pouvez retirer 1, 2 ou 3 batons à chaque tour.") 
    print("Il y a aussi un bot mais pas le droit à l'erreur !")
    sleep(5)
    print("\n")

def main():
    notice()
    bot = 2
    while bot != 0 and bot != 1:
        bot = int(input("Voulez-vous jouer contre un bot ? (Oui = 1, Non = 0))"))
    nbatons = randint(10, 20)
    print("Il y a", nbatons, "batons")
    trame(nbatons, bot)

if __name__ == "__main__":
    main()