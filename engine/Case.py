# <========== import ==========>

from __future__ import annotations
from json import dump, load

# <========== Local Import ==========>

from pygame import surface, rect, image, transform
from pygame.color import Color


# <========== class ==========>

class Case:
    """ The game is compose of a multiple number of case on a map
    """
    
    # <----- init ----->
    
    def __init__(self: Case, name: str, sprite: str | None, hitbox: bool, size: tuple[float, float], position: tuple[float, float], center: bool = False, color: Color | tuple[int,int,int] | tuple[int,int,int,int] | None = None) -> None:
        """The constructor.        

        Args:
            self (Case): self
            name (str): The case have a name to use for saving and loading.
            sprite (str | None): The case can have a sprite (the path to the sprite) or not if you just want a case with color for exemple.
            hitbox (bool): If the case have a hitbox or not.
            size (tuple[float, float]): Size of the case.
            position (tuple[float, float]): Position of the case on the map.
            center (bool, optional): Using if when you place the case, the position referer to the center of the case. Defaults to False.
            color (Color | tuple[int,int,int] | tuple[int,int,int,int] | None, optional): The color of the case. Defaults to None.
        """
        self.__name: str = name
        self.__sprite: str | None = sprite
        self.__hitbox: bool = hitbox
        self.__center: bool = center
        self.__color: Color | tuple[int,int,int] | tuple[int,int,int, int] | None = color
        
        
        self.__surface: surface.Surface = surface.Surface(size)
        if isinstance(sprite, str):
            self.__surface = image.load(sprite)
            self.__surface = transform.scale(self.__surface, size = size)
            
        
        if isinstance(color, Color): self.__surface.fill(color)
        elif isinstance(color, tuple):
            if len(color) == 4: self.__surface.fill(Color(color[0], color[1], color[2], color[3]))
            else: self.__surface.fill(Color(color[0],color[1],color[2]))
        
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
    def position(self: Case) -> tuple[float, float]:
        if self.__center: return self.__rect.center
        else: return (self.__rect.left, self.__rect.top)
    
    @property
    def rect(self: Case) -> rect.Rect: return self.__rect
    
    @property
    def center(self: Case) -> bool: return self.__center
    
    @property
    def size(self: Case) -> tuple[float, float]: return self.__rect.size
    
    @property
    def color(self: Case) -> Color | tuple[int,int,int] | tuple[int,int,int, int] | None: return self.__color
    
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
    def sprite(self: Case, new_sprite: str) -> None:
        self.__sprite = new_sprite
        self.__surface = image.load(self.__sprite)
        self.__surface = transform.scale(self.__surface, size = self.size)
        if self.__center: self.__rect = self.__surface.get_rect(center = self.position)
        else: self.__rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])
        
    @hitbox.setter
    def hitbox(self: Case, new_hitbox: bool) -> None: self.__hitbox = new_hitbox
    
    @surface.setter
    def surface(self: Case, new_surface) -> None: self.__surface = new_surface      
    
    @position.setter
    def position(self: Case, new_position: tuple[float, float]) -> None:
        if self.__center: self.__rect = self.__surface.get_rect(center = new_position)
        else: self.__rect = self.__surface.get_rect(x = new_position[0], y = new_position[1])
            
    @size.setter
    def size(self: Case, new_size: tuple[float, float]) -> None:
        if self.sprite != None: self.__surface = transform.scale(self.__surface, size = self.size)
        
        if self.__center: self.__rect = self.__surface.get_rect(center = self.position)
        else: self.__rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])
            
    @color.setter
    def color(self: Case, new_color: Color |tuple[int,int,int] | tuple[int,int,int, int]) -> None:
        self.__color = new_color
        if isinstance(new_color, Color): self.__surface.fill(new_color)
        elif isinstance(new_color, tuple):
            if len(new_color) == 4: self.__surface.fill(Color(new_color[0], new_color[1], new_color[2], new_color[3]))
            else: self.__surface.fill(Color(new_color[0], new_color[1], new_color[2]))
            
    # <----- save ----->
    
    def save(self: Case) -> None:
        """Save the case with json format.
        The file will be in 'data/case/{case_name}.json'.
        Only name, sprite, hitbox and color is save.

        Args:
            self (Case): self
        """
        with open(f"data/case/{self.__name}.json", "w+") as file:
            dump(self.__dict__, file)
            
    # <----- load ----->
    
    @staticmethod
    def load(case_name: str, size: tuple[float, float], position: tuple[float, float], center: bool = False) -> Case:
        """Load a json file in 'data/case{case_name}.json'

        Args:
            case_name (str): The case name
            size (tuple[float, float]): The size of the case.
            position (tuple[float, float]): The position of the case on the map.
            center (bool, optional): If position references the center of the case. Defaults to False.

        Returns:
            Case: the loaded case
        """
        with open(f"data/case/{case_name}.json", "r") as file:
            data: dict = load(file)
            return Case(data["name"], data["sprite"], data["hitbox"], size, position, center, (Color(data["color"][0], data["color"][1], data["color"][2], data["color"][3]) if isinstance(data["color"], list) else None))
        
        