from __future__ import annotations

from engine.SpriteSheet import SpriteSheet

class Entity:

    def __init__(self: Entity, name: str, position: tuple[float, float], sprite_sheet: SpriteSheet) -> None:
        self.name: str = name
        self.position: tuple[float, float] = position
        self.sprite_sheet: SpriteSheet = sprite_sheet