import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)

# Paramètres de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de Uno")

# Fonction principale du jeu
def jouer_uno():
    en_cours = True

    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False

        # Effacer l'écran
        fenetre.fill(BLANC)

        # Dessiner des éléments du jeu
        # En haut à gauche : les joueurs et leurs scores
        for i, joueur in enumerate(joueurs):
            texte_joueur = f"{joueur.nom} : {joueur.score}"
            surface_texte = pygame.font.SysFont(None, 24).render(texte_joueur, True, NOIR)
            fenetre.blit(surface_texte, (10, 10 + i * 30))

        # En bas : le deck de cartes du joueur
        deck_joueur = pygame.Surface((200, 100))
        deck_joueur.fill(BLEU)
        fenetre.blit(deck_joueur, (10, hauteur - 110))

        # Limiter le taux de rafraîchissement
        pygame.time.Clock().tick(30)

    # Quitter Pygame
    pygame.quit()
    sys.exit()




# Lancement du jeu
if __name__ == "__main__":
    jouer_uno()

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.score = 0

    def augmenter_score(self, points):
        self.score += points


couleurs = ["rouge", "bleu", "vert", "jaune"]
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Fonction de distribution des cartes aux joueurs
def distribution(joueurs, couleur, nombre):
    for joueur in joueurs: # Pour chaque joueur
        print(f"Distribution de la carte {couleur} {nombre} à {joueur.nom}") # Affichage de la carte distribuée

