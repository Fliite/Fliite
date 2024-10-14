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

        # Actualiser l'affichage
        pygame.display.flip()

        # Limiter le taux de rafraîchissement
        pygame.time.Clock().tick(30)

    # Quitter Pygame
    pygame.quit()
    sys.exit()

# Lancement du jeu
if __name__ == "__main__":
    jouer_uno()
