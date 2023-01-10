# <========== Import ==========>

from __future__ import annotations
from json import dumps, load
from os import listdir, mkdir
from os.path import exists

# <========== Class ==========>

class Tile():
    
    # <----- init ----->
    
    def __init__(self: Tile, sprite: str | None = None, hitbox: bool = False) -> None:
        self.__sprite: str | None= sprite
        self.__hitbox: bool = hitbox
        
    # <----- getter ----->
    
    @property
    def sprite(self: Tile) -> str | None: return self.__sprite
    
    @property
    def hitbox(self: Tile) -> bool: return self.__hitbox
    
    # <----- setter ----->
    
    @sprite.setter
    def sprite(self: Tile, new_sprite: str) -> None: self.__sprite = new_sprite
    
    @hitbox.setter
    def hitbox(self: Tile, new_hitbox: bool) -> None: self.__hitbox = new_hitbox
    
    # <----- str ----->
    
    def __str__(self: Tile) -> str: return f"{self.__sprite}"
    
    # <----- repr ----->
    
    def __repr__(self: Tile) -> str: return f"{self.__sprite}"