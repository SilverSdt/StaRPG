import pygame
import MovableCharacter

from engine.Case import Case
from engine.SpriteSheet import SpriteSheet

screen = pygame.display.set_mode((1920, 1080))

pygame.init()
clock = pygame.time.Clock()
background = (255, 255, 255)
loop = True

ss = SpriteSheet('assets/spritesheet/spritesheet.png', (0 ,0 , 64, 64))
c: Case = Case((1920/2, 1080/2), (64, 64), ss.image_at((0, 0, 64, 64)), True)

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill(background)

    screen.blit(c.surface, c.location)

    keys = pygame.key.get_pressed()
    MovableCharacter.control.__call__(screen, keys)


    pygame.display.flip()
    clock.tick(60)