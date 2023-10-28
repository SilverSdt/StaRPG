import pygame
import MovableCharacter

from engine.Case import Case
from engine.Map import Map

screen: pygame.surface.Surface = pygame.display.set_mode((1920, 1080))

pygame.init()
clock = pygame.time.Clock()
background = (255, 255, 255)
loop = True

cases: list[Case] = []
for i in range(0, 1920, 64):
    for j in range(0, 1080, 64):
        if (i + j) % 128 == 0:
            cases.append(Case((i, j), (64, 64), (0,0,0), False))

m: Map = Map("test field", cases)

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill(background)

    m.blit(screen)

    keys = pygame.key.get_pressed()
    MovableCharacter.control.__call__(screen, keys)


    pygame.display.flip()
    clock.tick(60)