# <========== import ==========>

from __future__ import annotations

from pygame import surface, rect, image, transform

# <========== class ==========>

class Entity:

    # <----- init ----->

    def __init__(self: Entity, name: str, sprite: str, size: tuple[float, float], position: tuple[float, float], center: bool = False) -> None:
        self.__name: str = name
        self.__sprite: str = sprite
        self.__center: bool = center

        self.__surface: surface.Surface = surface.Surface(size)
        self.__surface = image.load(sprite)
        self.__surface = transform.scale(self.__surface, size = size)

        if center: self.__rect: rect.Rect = self.__surface.get_rect(center = position)
        else: self.__rect: rect.Rect = self.__surface.get_rect(x = position[0], y = position[1])

    # <----- getter ----->

    @property
    def name(self: Entity) -> str: return self.__name

    @property
    def sprite(self: Entity) -> str: return self.__sprite

    @property
    def size(self: Entity) -> tuple[float, float]: return self.__rect.size

    @property
    def position(self: Entity) -> tuple[float, float]:
        if self.__center: return self.__rect.center
        else: return (self.__rect.left, self.__rect.top)

    @property
    def center(self: Entity) -> bool: return self.__center

    @property
    def surface(self: Entity) -> surface.Surface: return self.__surface

    @property
    def rect(self: Entity) -> rect.Rect: return self.__rect

    # <----- setter ----->

    @name.setter
    def name(self: Entity, new_name: str) -> None: self.__name = new_name

    @sprite.setter
    def sprite(self: Entity, new_sprite: str) -> None:
        self.__sprite = new_sprite

        self.__surface = image.load(self.__sprite)
        self.__surface = transform.scale(self.__surface, size = self.__rect.size)
        if self.__center: self.__rect = self.__surface.get_rect(center = self.position)
        else: self.__rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])


    @size.setter
    def size(self: Entity, new_size: tuple[float, float]) -> None:
        self.__surface = transform.scale(self.__surface, size = new_size)

        if self.__center: self.__rect = self.__surface.get_rect(center = self.position)
        else: self.__rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])

    @position.setter
    def position(self: Entity, new_position: tuple[float, float]) -> None:
        if self.__center: self.__rect = self.__surface.get_rect(center = new_position)
        else: self.__rect = self.__surface.get_rect(x = new_position[0], y = new_position[1])

    @center.setter
    def center(self: Entity, new_center: bool) -> None:
        self.__center = new_center

        if self.__center: self.__rect = self.__surface.get_rect(center = (self.__rect.x, self.__rect.y))
        else: self.__rect = self.__surface.get_rect(x = self.__rect.center[0], y = self.__rect.center[1])



