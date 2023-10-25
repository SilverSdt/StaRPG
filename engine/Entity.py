# <========== Import ==========>

from __future__ import annotations

# <========== Local Import ==========>

from engine.SpriteSheet import SpriteSheet

# <========== Class ==========>

class Entity:

    def __init__(self: Entity, name: str, position: tuple[float, float], sprite_sheet: SpriteSheet, size: tuple[float, float],speed: int = 0) -> None:
        self.name: str = name
        self.position: tuple[float, float] = position
        self.sprite_sheet: SpriteSheet = sprite_sheet
        self.size: tuple[float, float] = size
        self.speed: int = speed