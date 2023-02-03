import pygame
from sys import exit

from engine.Map import Map
from engine.Entity import Entity


# initialise les module de la bibliotheque
pygame.init()

# definition de la fenetre de jeu
screen: pygame.surface.Surface = pygame.display.set_mode((1280, 720), pygame.RESIZABLE | pygame.SCALED)
        
map: Map = Map.load("grass test map", (1280,720))
mario: Entity = Entity("mario", "asset/entity/mario.png", (400,400), (1280/2, 720/2), True)

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
    screen.blit(mario.surface, mario.rect)
    
    # mise a jour de l'affichage de la fenetre de jeu
    pygame.display.update()
    
    # definition des fps
    cloak.tick(60)