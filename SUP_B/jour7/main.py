#importation des foncions
import tribulle as tri
import listehasard as lis
import show as sho
import count as cou

def main():
    L = lis.deflis(100, -20, 30) #liste aléatoire
    Y = tri.tribulle(L) #liste triée en mode tri bulle
    Z = cou.count(Y) #compte de la liste triée
    X = [i for i in range(100)] #liste de 0 à 99 en guise d'ordonnées
    sho.graph(X, Y) #affichage du graphique
    sho.graph2(X, Z) #affichage du graphique 2
    

    
if __name__ == '__main__':
    main()