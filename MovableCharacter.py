import pygame
from typing import Any, Sequence

from engine.Animation import Animation
from engine.Entity import Entity
from engine.SpriteSheet import SpriteSheet

from CreateCamera import camera
from CreateMap import m



tick: int = 5
animations: list[Animation] = [
    Animation((0, 0, 64, 64), [(64, 0, 64, 64, tick), (128, 0, 64, 64, tick), (192, 0, 64, 64, tick), (0, 0, 64, 64, tick)], pygame.K_DOWN),
    Animation((0, 64, 64, 64), [(64, 64, 64, 64, tick), (128, 64, 64, 64, tick), (192, 64, 64, 64, tick), (0, 64, 64, 64, tick)], pygame.K_LEFT),
    Animation((0, 128, 64, 64), [(64, 128, 64, 64, tick), (128, 128, 64, 64, tick), (192, 128, 64, 64, tick), (0, 128, 64, 64, tick)], pygame.K_RIGHT),
    Animation((0, 192, 64, 64), [(64, 192, 64, 64, tick), (128, 192, 64, 64, tick), (192, 192, 64, 64, tick), (0, 192, 64, 64, tick)], pygame.K_UP)
]
ss = SpriteSheet('assets/spritesheet/spritesheet.png', (0 ,0 , 64, 64), animations)
mc: Entity = Entity("Red", (928, 508), ss, (100, 100), 5)

key: int | None = None

def move(canvas: pygame.surface.Surface, keys: Sequence[bool]) -> None:
    global key

    if keys[pygame.K_LEFT] and (key == None or key == pygame.K_LEFT):
        if mc.position[0] - mc.speed > 0: mc.position = (mc.position[0] - mc.speed, mc.position[1])
        key = pygame.K_LEFT
    elif keys[pygame.K_RIGHT] and (key == None or key == pygame.K_RIGHT):
        if mc.position[0] + mc.speed + mc.size[0] < canvas.get_size()[0] :mc.position = (mc.position[0] + mc.speed, mc.position[1])
        key = pygame.K_RIGHT
    elif keys[pygame.K_DOWN] and (key == None or key == pygame.K_DOWN):
        if mc.position[1] + mc.speed + mc.size[1] < canvas.get_size()[1]: mc.position = (mc.position[0], mc.position[1] + mc.speed)
        key = pygame.K_DOWN
    elif keys[pygame.K_UP] and (key == None or key == pygame.K_UP):
        if mc.position[1] - mc.speed > 0: mc.position = (mc.position[0], mc.position[1] - mc.speed)
        key = pygame.K_UP
    else:
        key = None

    sprite: pygame.surface.Surface = mc.sprite_sheet.next(key)
    sprite = pygame.transform.scale(sprite, mc.size)

    m.blit(canvas, (255,255,255), camera.offset)
    canvas.blit(sprite, (mc.position[0] - camera.offset.x, mc.position[1] - camera.offset.y))

