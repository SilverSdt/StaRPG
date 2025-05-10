import pygame
from typing import Any, Sequence

from engine.Animation import Animation
from engine.Entity import Entity
from engine.SpriteSheet import SpriteSheet

from CreateCamera import camera
from CreateMap import m



tick: int = 5

animations_dict: dict[str, Animation] = {
    "down": Animation([(64, 0, 64, 64, tick), (128, 0, 64, 64, tick), (192, 0, 64, 64, tick), (0, 0, 64, 64, tick)]),
    "left": Animation([(64, 64, 64, 64, tick), (128, 64, 64, 64, tick), (192, 64, 64, 64, tick), (0, 64, 64, 64, tick)]),
    "right": Animation([(64, 128, 64, 64, tick), (128, 128, 64, 64, tick), (192, 128, 64, 64, tick), (0, 128, 64, 64, tick)]),
    "up": Animation([(64, 192, 64, 64, tick), (128, 192, 64, 64, tick), (192, 192, 64, 64, tick), (0, 192, 64, 64, tick)])
}

states_dist: dict[str, tuple[int, int, int, int]] = {
    "down_idle": (0, 0, 64, 64),
    "left_idle": (0, 64, 64, 64),
    "right_idle": (0, 128, 64, 64),
    "up_idle": (0, 192, 64, 64)
}

sprite_sheet = SpriteSheet('assets/spritesheet/spritesheet.png')
mc: Entity = Entity("Red", (928, 508), sprite_sheet, (100, 100), 5)

key: str = ""
position: str = "down"

def move(canvas: pygame.surface.Surface, keys: Sequence[bool]) -> None:
    global key
    global position

    if keys[pygame.K_LEFT] and (key == "" or key == "left"):
        mc.position = (mc.position[0] - mc.speed, mc.position[1])
        key = position = "left"
        sprite: pygame.surface.Surface = mc.sprite_sheet.next(key, animations_dict)

    elif keys[pygame.K_RIGHT] and (key == "" or key == "right"):
        mc.position = (mc.position[0] + mc.speed, mc.position[1])
        key = position = "right"
        sprite: pygame.surface.Surface = mc.sprite_sheet.next(key, animations_dict)

    elif keys[pygame.K_DOWN] and (key == "" or key == "down"):
        mc.position = (mc.position[0], mc.position[1] + mc.speed)
        key = position = "down"
        sprite: pygame.surface.Surface = mc.sprite_sheet.next(key, animations_dict)

    elif keys[pygame.K_UP] and (key == "" or key == "up"):
        mc.position = (mc.position[0], mc.position[1] - mc.speed)
        key = position = "up"
        sprite: pygame.surface.Surface = mc.sprite_sheet.next(key, animations_dict)

    else:
        sprite: pygame.surface.Surface = mc.sprite_sheet.image_at(states_dist[f"{position}_idle"])
        key = ""

    sprite = pygame.transform.scale(sprite, mc.size)
    m.blit(canvas, (255,255,255), camera.offset)
    canvas.blit(sprite, (mc.position[0] - camera.offset.x, mc.position[1] - camera.offset.y))

