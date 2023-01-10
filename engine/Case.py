# <========== import ==========>

from __future__ import annotations
from pygame import surface, rect, image, transform

from engine.Tile import Tile

# <========== class ==========>

class Case:
    
    # <----- init ----->
    
    def __init__(self: Case, tile: Tile, size: tuple[float, float], position: tuple[float, float], center: bool = True) -> None:
        self.__surface: surface.Surface = surface.Surface(size)
        if tile.sprite != None:
            self.__surface = image.load(tile.sprite)
            self.__surface = transform.scale(self.__surface, size = size)
        
        
        self.__tile: Tile = tile
        self.__center: bool = center
        self.__size: tuple[float, float] = size
        self.__position: tuple[float, float] = position
        
        if center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(x = position[0], y = position[1])


    # <----- getter -----> 
    
    @property
    def surface(self: Case) -> surface.Surface: return self.__surface
    
    @property
    def tile(self: Case) -> Tile: return self.__tile
    
    @property
    def position(self: Case) -> tuple[float, float]: return self.__position
    
    @property
    def rect(self: Case) -> rect.Rect: return self.__rect
    
    @property
    def center(self: Case) -> bool: return self.__center
    
    @property
    def size(self: Case) -> tuple[float, float]: return self.__size
    
    # <----- setter ----->
    
    @surface.setter
    def surface(self: Case, new_surface) -> None: self.__surface = new_surface
    
    @tile.setter
    def tile(self: Case, new_tile: Tile) -> None:
        self.__tile = new_tile
        if self.__tile.sprite != None:
            self.__surface = image.load(self.__tile.sprite)
            self.__surface = transform.scale(self.__surface, size = self.__size)
            
    
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
        
        if self.tile.sprite != None:
            self.__surface = image.load(self.tile.sprite)
            self.__surface = transform.scale(self.__surface, size = self.size)
            
        if self.center:
            self.__rect: rect.Rect = self.__surface.get_rect(center = self.position)
        else:
            self.__rect: rect.Rect = self.__surface.get_rect(x = self.position[0], y = self.position[1])