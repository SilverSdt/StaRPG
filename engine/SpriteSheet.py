from __future__ import annotations

from typing import Sequence

import pygame

from engine.Animation import Animation


class SpriteSheet:

    def __init__(self: SpriteSheet, sprite_sheet_path: str, animations: list[Animation] | None = None) -> None:
        self.sheet: pygame.surface.Surface = pygame.image.load(
            sprite_sheet_path)
        self.animations: list[Animation] = animations.copy(
        ) if animations != None else []
        self.initial_state: tuple[int, int, int, int] = (0, 0, 64, 64)

    def image_at(self: SpriteSheet, rectangle: tuple[float, float, float, float]) -> pygame.surface.Surface:
        rect: pygame.Rect = pygame.Rect(rectangle)
        image: pygame.surface.Surface = pygame.Surface(
            rect.size, pygame.SRCALPHA, 32)
        image.blit(self.sheet, (0, 0), rect)

        return image

    def next(self: SpriteSheet, key: int | None) -> pygame.surface.Surface:
        if key != None:
            for animation in self.animations:
                if animation.state == True and ((animation.trigger != None and key == animation.trigger) or animation.trigger == None):
                    self.initial_state = animation.initial_stance

                    for anim in self.animations:
                        if anim != animation:
                            anim.state = False

                    return self.image_at(next(animation))

        for animation in self.animations: animation.state = True
        return self.image_at(self.initial_state)
