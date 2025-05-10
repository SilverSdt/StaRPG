# <========== Import ==========>

from __future__ import annotations
from typing import Sequence
import pygame

# <========== Local Import ==========>

from engine.Animation import Animation


# <========== Class ==========>

class SpriteSheet:

    def __init__(self: SpriteSheet, sprite_sheet_path: str) -> None:
        self.sheet: pygame.surface.Surface = pygame.image.load(sprite_sheet_path)

    def image_at(self: SpriteSheet, rectangle: tuple[float, float, float, float]) -> pygame.surface.Surface:
        rect: pygame.Rect = pygame.Rect(rectangle)
        image: pygame.surface.Surface = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        image.blit(self.sheet, (0, 0), rect)

        return image

    def next(self: SpriteSheet, key: int | None, animations_dict: dict[str, Animation]) -> pygame.surface.Surface:
        if key in animations_dict:
                return self.image_at(next(animations_dict[key]))

