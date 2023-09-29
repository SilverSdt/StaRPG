import pygame

from engine.Animation import Animation
from engine.Entity import Entity
from engine.SpriteSheet import SpriteSheet

fenetre = pygame.display.set_mode((1920, 1080))

pygame.init()
clock = pygame.time.Clock()

tick: int = 5
speed: int = 10

animations: list[Animation] = [
    Animation((0, 0, 64, 64), [(64, 0, 64, 64, tick), (128, 0, 64, 64, tick), (192, 0, 64, 64, tick), (0, 0, 64, 64, tick)], pygame.K_DOWN),
    Animation((0, 64, 64, 64), [(64, 64, 64, 64, tick), (128, 64, 64, 64, tick), (192, 64, 64, 64, tick), (0, 64, 64, 64, tick)], pygame.K_LEFT),
    Animation((0, 128, 64, 64), [(64, 128, 64, 64, tick), (128, 128, 64, 64, tick), (192, 128, 64, 64, tick), (0, 128, 64, 64, tick)], pygame.K_RIGHT),
    Animation((0, 192, 64, 64), [(64, 192, 64, 64, tick), (128, 192, 64, 64, tick), (192, 192, 64, 64, tick), (0, 192, 64, 64, tick)], pygame.K_UP)
]
ss = SpriteSheet('assets/spritesheet/spritesheet.png', animations)
red: Entity = Entity("Red", (920, 540), ss)

background = (255, 255, 255)
loop = True
key: int | None = None

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            pass

    fenetre.fill(background)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (key == None or key == pygame.K_LEFT):
        red.position = (red.position[0] - speed, red.position[1])
        key = pygame.K_LEFT
    elif keys[pygame.K_RIGHT] and (key == None or key == pygame.K_RIGHT):
        red.position = (red.position[0] + speed, red.position[1])
        key = pygame.K_RIGHT
    elif keys[pygame.K_DOWN] and (key == None or key == pygame.K_DOWN):
        red.position = (red.position[0], red.position[1] + speed)
        key = pygame.K_DOWN
    elif keys[pygame.K_UP] and (key == None or key == pygame.K_UP):
        red.position = (red.position[0], red.position[1] - speed)
        key = pygame.K_UP
    else:
        key = None

    fenetre.blit(red.sprite_sheet.next(key), red.position)


    pygame.display.flip()
    clock.tick(60)
