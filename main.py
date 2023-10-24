import pygame
import MovableCharacter

screen = pygame.display.set_mode((1920, 1080))

pygame.init()
clock = pygame.time.Clock()
background = (255, 255, 255)
loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill(background)

    keys = pygame.key.get_pressed()
    MovableCharacter.control.__call__(screen, keys)


    pygame.display.flip()
    clock.tick(60)