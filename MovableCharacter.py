from typing import Any, Sequence

from engine.Animation import Animation
from engine.Control import Control
from engine.Entity import Entity
from engine.SpriteSheet import SpriteSheet
import pygame


tick: int = 5
animations: list[Animation] = [
    Animation((0, 0, 64, 64), [(64, 0, 64, 64, tick), (128, 0, 64, 64, tick), (192, 0, 64, 64, tick), (0, 0, 64, 64, tick)], pygame.K_DOWN),
    Animation((0, 64, 64, 64), [(64, 64, 64, 64, tick), (128, 64, 64, 64, tick), (192, 64, 64, 64, tick), (0, 64, 64, 64, tick)], pygame.K_LEFT),
    Animation((0, 128, 64, 64), [(64, 128, 64, 64, tick), (128, 128, 64, 64, tick), (192, 128, 64, 64, tick), (0, 128, 64, 64, tick)], pygame.K_RIGHT),
    Animation((0, 192, 64, 64), [(64, 192, 64, 64, tick), (128, 192, 64, 64, tick), (192, 192, 64, 64, tick), (0, 192, 64, 64, tick)], pygame.K_UP)
]
ss = SpriteSheet('assets/spritesheet/spritesheet.png', animations)
red: Entity = Entity("Red", (920, 540), ss, 5)

variables: dict[str, Any] = {
    "key": None
}

def func(entity: Entity, fenetre: pygame.surface.Surface, keys: Sequence[bool], key: int | None) -> None:
    if keys[pygame.K_LEFT] and (key == None or key == pygame.K_LEFT):
        entity.position = (entity.position[0] - entity.speed, entity.position[1])
        key = pygame.K_LEFT
    elif keys[pygame.K_RIGHT] and (key == None or key == pygame.K_RIGHT):
        entity.position = (entity.position[0] + entity.speed, entity.position[1])
        key = pygame.K_RIGHT
    elif keys[pygame.K_DOWN] and (key == None or key == pygame.K_DOWN):
        entity.position = (entity.position[0], entity.position[1] + entity.speed)
        key = pygame.K_DOWN
    elif keys[pygame.K_UP] and (key == None or key == pygame.K_UP):
        entity.position = (entity.position[0], entity.position[1] - entity.speed)
        key = pygame.K_UP
    else:
        key = None

    fenetre.blit(control.entity.sprite_sheet.next(key), control.entity.position)

control: Control = Control(red, func, variables)