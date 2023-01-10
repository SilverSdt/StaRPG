import pygame
from sys import exit

from engine.Case import Case
from engine.Tile import Tile


# initialise les module de la bibliotheque
pygame.init()

# definition de la fenetre de jeu
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)

white_case: Case = Case(Tile("asset/tile/grass.jpeg"), (200, 200), (1280/2, 720/2))

# definition de la cloak
cloak = pygame.time.Clock()

# game loop
game_on = True
while(game_on):
    
    # boucle pour les events du jeu
    for event in pygame.event.get():
        # event pour quitter le jeu
        if event.type ==pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(white_case.surface, white_case.rect)
    
    # mise a jour de l'affichage de la fenetre de jeu
    pygame.display.update()
    
    # definition des fps
    cloak.tick(60)