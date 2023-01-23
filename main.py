import pygame
from sys import exit

from engine.Case import Case
from engine.Map import Map


# initialise les module de la bibliotheque
pygame.init()

# definition de la fenetre de jeu
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)

white_case: Case = Case("asset/tile/grass.jpeg", False, (200, 200), (1280/2, 720/2))
white_case.size = (50,50)

liste: list = []
for i in range(10):
    for j in range(10):
        liste.append(("grass", (i,j)))
        
map: Map = Map(liste, (10,10), (1280,720), (2, 2))
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
    
    for case in map.case_list:
        screen.blit(case.surface, case.rect)
    
    # mise a jour de l'affichage de la fenetre de jeu
    pygame.display.update()
    
    # definition des fps
    cloak.tick(60)