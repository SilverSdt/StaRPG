# <========== import ==========>

from __future__ import annotations

from pygame import surface, rect, image, transform
from pygame.color import Color
from json import dump, load

# <========== class ==========>

class Case:
    
    # <----- init ----->
    
    def __init__(self: Case, name: str, sprite: str | None, hitbox: bool, size: tuple[float, float], position: tuple[float, float], center: bool = False, color: Color | None = None) -> None:
        self.__name: str = name
        self.__surface: surface.Surface = surface.Surface(size)
        self.__sprite: str | None = None
        if isinstance(sprite, str):
            self.__surface = image.load(sprite)
            self.__surface = transform.scale(self.__surface, size = size)
            self.__sprite = sprite
        elif isinstance(sprite, Color):
            self.__surface.fill(sprite)
        
        
        self.__hitbox: bool = hitbox
        self.__center: bool = center
        self.__size: tuple[float, float] = size
        self.__position: tuple[float, float] = position
        self.__color: Color | None = color
        if isinstance(color, Color): self.__surface.fill(color)
        
        if center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(x = position[0], y = position[1])

    # <----- getter -----> 
    
    @property
    def name(self: Case) -> str: return self.__name
    
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
    def color(self: Case) -> Color | None: return self.__color
    
    @property
    def __dict__(self: Case) -> dict[str, object]:
        return {
            "name": self.__name,
            "sprite": self.__sprite,
            "hitbox": self.__hitbox,
            "color": ([self.__color.r, self.__color.g, self.__color.b, self.__color.a]if isinstance(self.__color, Color) else None)
        }
    
    # <----- setter ----->
    
    @name.setter
    def name(self: Case, new_name: str) -> None: self.__name = new_name
    
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
            
    @color.setter
    def color(self: Case, new_color: Color) -> None:
        self.__color = new_color
        self.__surface.fill(new_color)
            
    # <----- save ----->
    
    def save(self: Case) -> None:
        with open(f"data/case/{self.__name}.json", "w+") as file:
            dump(self.__dict__, file)
            
    # <----- load ----->
    
    @staticmethod
    def load(case_name: str, size: tuple[float, float], position: tuple[float, float], center: bool = False) -> Case:
        with open(f"data/case/{case_name}.json", "r") as file:
            data: dict = load(file)
            return Case(data["name"], data["sprite"], data["hitbox"], size, position, center, (Color(data["color"][0], data["color"][1], data["color"][2], data["color"][3]) if isinstance(data["color"], list) else None))
        
        