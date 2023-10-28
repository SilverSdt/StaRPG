# <========== Imports ==========>

from __future__ import annotations
import pygame

# <========== Local Imports ==========>

from engine.Case import Case

# <========== Class ==========>

class Map:

    def __init__(self: Map, name: str, cases: list[Case] | None = None):
        self.name: str = name
        self.cases: list[Case] = cases.copy() if cases != None else []

    def blit(self: Map, screen: pygame.surface.Surface) -> None:
        for case in self.cases:
            screen.blit(case.surface, case.location)