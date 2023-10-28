# <========== Imports ==========>

from __future__ import annotations
import pygame

# <========== Class ==========>

class Case:

    def __init__(self: Case, location: tuple[float, float], size: tuple[float, float], sprite: pygame.surface.Surface | pygame.color.Color | tuple[int, int, int], hitbox: bool) -> None:
        self.location: tuple[float, float] = location
        self.hitbox: bool = hitbox

        if isinstance(sprite, pygame.surface.Surface):
            self.surface: pygame.surface.Surface = sprite
        else:
            self.surface: pygame.surface.Surface = pygame.surface.Surface(size)
            self.surface.fill(sprite)
        self.surface = pygame.transform.scale(self.surface, size)

    @property
    def size(self: Case) -> tuple[float, float]:
        return self.surface.get_size()

    @property
    def x(self: Case) -> float:
        return self.location[0]

    @property
    def y(self: Case) -> float:
        return self.location[1]

    @size.setter
    def size(self: Case, size: tuple[float, float]) -> None:
        self.surface = pygame.transform.scale(self.surface, size)

    @x.setter
    def x(self: Case, x: float) -> None:
        self.location = (x, self.location[1])

    @y.setter
    def y(self: Case, y: float) -> None:
        self.location = (self.location[0], y)

    def is_on_contact(self: Case, other_location: tuple[float, float], other_size: tuple[int, int]) -> bool:

        if self.hitbox:
            sprite = pygame.sprite.Sprite()
            sprite.image = self.surface
            sprite.rect = sprite.image.get_rect(topleft=self.location)
            return bool(pygame.rect.Rect(other_location, other_size).colliderect(sprite.rect))
        else:
            return False