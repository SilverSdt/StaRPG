from random import randint

import pygame

from engine.Animation import Animation
from engine.Entity import Entity
from engine.SpriteSheet import SpriteSheet

fenetre = pygame.display.set_mode((1920, 1080))

pygame.init()
clock = pygame.time.Clock()

tick: int = 5
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
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    fenetre.fill(background)

    keys = pygame.key.get_pressed()
    fenetre.blit(red.sprite_sheet.next(keys), red.position)

    if keys[pygame.K_LEFT]: red.position = (red.position[0] - 10, red.position[1])
    if keys[pygame.K_RIGHT]: red.position = (red.position[0] + 10, red.position[1])
    if keys[pygame.K_DOWN]: red.position = (red.position[0], red.position[1] + 10)
    if keys[pygame.K_UP]: red.position = (red.position[0], red.position[1] - 10)
    if keys[pygame.K_a]: red.position = (randint(0,1920), randint(0,1080))


    pygame.display.flip()
    clock.tick(60)
