import pygame
import MovableCharacter

screen: pygame.surface.Surface = pygame.display.set_mode((1920, 1080))
canvas: pygame.surface.Surface = pygame.display.set_mode((1920, 1080))

screen.fill((0, 0, 0))
canvas.fill((255, 255, 255))

pygame.init()
clock = pygame.time.Clock()
loop = True

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    screen.fill((0, 0, 0))

    keys = pygame.key.get_pressed()
    MovableCharacter.move(canvas, keys)
    MovableCharacter.camera.scroll(MovableCharacter.mc)

    screen.blit(canvas, (0, 0))
    pygame.display.flip()
    clock.tick(60)