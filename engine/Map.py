# <========== import ==========>

from __future__ import annotations

from engine.Case import Case

# <========== class ==========>

class Map:
    
    # <----- init ----->
    
    def __init__(self: Map, case_list: list[Case], position: tuple[float, float], orientation: int, grid_size: tuple[int, int], screen_size: tuple[int, int]) -> None:
        self.__case_list: list[Case] = case_list.copy()
        self.__position: tuple[float, float] = position
        self.__orientation: int = orientation
        self.__grid_size: tuple[int, int] = grid_size
        self.__screen_size: tuple[int, int] = screen_size
        
    # <----- getter ----->
    
    @property
    def case_list(self: Map) -> list[Case]: return self.__case_list
    
    @property
    def position(self: Map) -> tuple[float, float]: return self.__position
    
    @property
    def orientation(self: Map) -> int: return self.__orientation
    
    @property
    def grid_size(self: Map) -> tuple[int, int]: return self.__grid_size
    
    @property
    def screen_size(self: Map) -> tuple[int, int]: return self.__screen_size
    
    # <----- setter ----->
    
    @case_list.setter
    def case_list(self: Map, new_case_list: list[Case]) -> None: self.__case_list = new_case_list.copy()
    
    @position.setter
    def position(self: Map, new_position: tuple[float, float]) -> None: self.__position = new_position
    
    @orientation.setter
    def orientation(self: Map, new_orientation: int) -> None: self.__orientation = new_orientation
    
    @grid_size.setter
    def grid_size(self: Map, new_grid_size: tuple[int, int]) -> None: self.__grid_size = new_grid_size
    
    @screen_size.setter
    def screen_size(self: Map, new_screen_size: tuple[int, int]) -> None: self.__screen_size = new_screen_size
        



