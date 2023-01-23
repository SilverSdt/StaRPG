# <========== import ==========>

from __future__ import annotations

from pygame import surface, rect, image, transform
from json import dump

# <========== class ==========>

class Case:
    
    # <----- init ----->
    
    def __init__(self: Case, sprite: str | None, hitbox: bool, size: tuple[float, float], position: tuple[float, float], center: bool = False) -> None:
        self.__surface: surface.Surface = surface.Surface(size)
        if sprite != None:
            self.__surface = image.load(sprite)
            self.__surface = transform.scale(self.__surface, size = size)
        
        
        self.__sprite: str | None = sprite
        self.__hitbox: bool = hitbox
        self.__center: bool = center
        self.__size: tuple[float, float] = size
        self.__position: tuple[float, float] = position
        
        if center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(x = position[0], y = position[1])

    # <----- getter -----> 
    
    @property
    def sprite(self: Case) -> str | None: return self.__sprite
    
    @property
    def hitbox(self: Case) -> bool: return self.__hitbox
    
    @property
    def surface(self: Case) -> surface.Surface: return self.__surface
    
    @property
    def position(self: Case) -> tuple[float, float]: return self.__position
    
    @property
    def rect(self: Case) -> rect.Rect: return self.__rect
    
    @property
    def center(self: Case) -> bool: return self.__center
    
    @property
    def size(self: Case) -> tuple[float, float]: return self.__size
    
    @property
    def __dict__(self: Case) -> dict[str, object]:
        return {
            "sprite": self.__sprite,
            "hitbox": self.__hitbox
        }
    
    # <----- setter ----->
    
    @sprite.setter
    def sprite(self: Case, new_sprite: str) -> None: self.__sprite = new_sprite
    
    @hitbox.setter
    def hitbox(self: Case, new_hitbox: bool) -> None: self.__hitbox = new_hitbox
    
    @surface.setter
    def surface(self: Case, new_surface) -> None: self.__surface = new_surface      
    
    @position.setter
    def position(self: Case, new_position: tuple[float, float]) -> None:
        self.__position = new_position
        if self.center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = new_position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(position = new_position)
            
    @size.setter
    def size(self: Case, new_size: tuple[float, float]) -> None:
        self.__size = new_size
        
        if self.sprite != None:
            self.__surface = image.load(self.sprite)
            self.__surface = transform.scale(self.__surface, size = self.size)
            
        if self.center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = self.position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])
            
    # <----- dict ----->
    
    def save(self: Case, case_name: str) -> None:
        with open(f"asset/case/{case_name}.json", "w+") as file:
            dump(self.__dict__, file)
        