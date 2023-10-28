# <========== Imports ==========>

from __future__ import annotations
import pygame

# <========== Local Imports ==========>

from engine.Case import Case

# <========== Type Alias ==========>

vec = pygame.math.Vector2

# <========== Class ==========>

class Map:

    def __init__(self: Map, name: str, cases: list[Case] | None = None) -> None:
        self.name: str = name
        self.cases: list[Case] = cases.copy() if cases != None else []

    def blit(self: Map, canvas: pygame.surface.Surface, fill_color = (0,0,0), offset: vec = vec(0,0)) -> None:
        map_surface: pygame.surface.Surface =  pygame.surface.Surface(canvas.get_size())
        map_surface.fill(fill_color)
        for case in self.cases:
            map_surface.blit(case.surface, case.location)

        canvas.blit(map_surface, (0 - offset.x, 0 - offset.y))