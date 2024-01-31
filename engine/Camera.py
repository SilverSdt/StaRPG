# <========== Imports ==========>

from __future__ import annotations
import pygame
from abc import ABC, abstractmethod
# <========== Local Imports ==========>

from engine.Entity import Entity

# <========== Type Alias ==========>

vec = pygame.math.Vector2

# <========== Class ==========>

class Camera:

    def __init__(self: Camera, display_width: int, display_height: int, const: vec | tuple[int, int] = vec(0,0)) -> None:
        self.offset: vec = vec(0, 0)
        self.offset_float: vec = vec(0, 0)
        self.display_width: int = display_width
        self.discplay_height: int = display_height
        self.CONST: vec = const if isinstance(const, vec) else vec(const[0], const[1])

    def setmethod(self: Camera, method: CamScroll) -> None:
        self.method: CamScroll = method

    def scroll(self: Camera, entity: Entity) -> None:
        self.method.scroll(entity)

class CamScroll(ABC):

    def __init__(self: CamScroll, camera: Camera)-> None:
        self.camera: Camera = camera

    @abstractmethod
    def scroll(self: CamScroll, entity: Entity) -> None:
        pass

class Follow(CamScroll):

        def __init__(self: Follow, camera: Camera) -> None:
            super().__init__(camera)

        def scroll(self: Follow, entity: Entity) -> None:
            self.camera.offset_float.x += (entity.position[0] - self.camera.offset_float.x - (self.camera.display_width / 2 - entity.size[0] / 2) + self.camera.CONST.x)
            self.camera.offset_float.y += (entity.position[1] - self.camera.offset_float.y - (self.camera.discplay_height / 2- entity.size[1] / 2) + self.camera.CONST.y)
            self.camera.offset.x = int(self.camera.offset_float.x)
            self.camera.offset.y = int(self.camera.offset_float.y)

class BorderFollow(CamScroll):

    def __init__(self: BorderFollow, camera: Camera, min: vec | tuple[int, int], max: vec | tuple[int, int]) -> None:
        super().__init__(camera)
        self.max: vec = max if max is vec else vec(max[0], max[1])
        self.min: vec = min if min is vec else vec(min[0], min[1])

    def scroll(self: BorderFollow, entity: Entity) -> None:


        if entity.position[0] > self.max.x:
            self.camera.offset_float.x += (entity.position[0] - self.camera.offset_float.x - (self.camera.display_width / 2 - entity.size[0] / 2) + self.camera.CONST.x)
        elif entity.position[0] < self.min.x:
            self.camera.offset_float.x += (entity.position[0] - self.camera.offset_float.x - (self.camera.display_width / 2 - entity.size[0] / 2) + self.camera.CONST.x)

        self.camera.offset.x = int(self.camera.offset_float.x)

        if entity.position[1] > self.max.y:
            self.camera.offset_float.y += (entity.position[1] - self.camera.offset_float.y - (self.camera.discplay_height / 2- entity.size[1] / 2) + self.camera.CONST.y)
        elif entity.position[1] < self.min.y:
            self.camera.offset_float.y += (entity.position[1] - self.camera.offset_float.y - (self.camera.discplay_height / 2- entity.size[1] / 2) + self.camera.CONST.y)

        self.camera.offset.y = int(self.camera.offset_float.y)

