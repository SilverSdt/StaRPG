# <========== import ==========>

from __future__ import annotations

from json import load

from engine.Case import Case

# <========== class ==========>

class Map:
    
    # <----- init ----->
    
    def __init__(self: Map, case_list: list[tuple[str, tuple[int, int]]], grid_size: tuple[int, int], screen_size: tuple[int, int] , case_on_screen: tuple[int, int]) -> None:
        self.__grid_size: tuple[int, int] = grid_size
        self.__screen_size: tuple[int, int] = screen_size
        self.__case_on_screen: tuple[int, int] = case_on_screen
        self.__case_list: list[Case] = []
        
        for case in case_list:
            with open(f"asset/case/{case[0]}.json", "r") as file:
                data: dict = load(file)
                self.__case_list.append(Case(data["sprite"], data["hitbox"], (screen_size[0] // case_on_screen[0], screen_size[1] // case_on_screen[1]), (case[1][0] * (screen_size[0] // case_on_screen[0]), case[1][1] * (screen_size[1] // case_on_screen[1]))))
        
        
    # <----- getter ----->
    
    @property
    def case_list(self: Map) -> list[Case]: return self.__case_list
    
    @property
    def grid_size(self: Map) -> tuple[int, int]: return self.__grid_size
    
    @property
    def screen_size(self: Map) -> tuple[int, int]: return self.__screen_size
    
    @property
    def case_on_screen(self: Map) -> tuple[int, int]: return self.__case_on_screen
    
    # <----- setter ----->
    
    @case_list.setter
    def case_list(self: Map, new_case_list: list[Case]) -> None: self.__case_list = new_case_list.copy()
    
    @grid_size.setter
    def grid_size(self: Map, new_grid_size: tuple[int, int]) -> None: self.__grid_size = new_grid_size
    
    @screen_size.setter
    def screen_size(self: Map, new_screen_size: tuple[int, int]) -> None: self.__screen_size = new_screen_size
    
    @case_on_screen.setter
    def case_on_screen(self: Map, new_case_on_screen: tuple[int, int]) -> None: self.__case_on_screen = new_case_on_screen
        
    # <----- get case by position ----->
    
    def get_case_by_position(self: Map, position: tuple[float, float]) -> Case | None:
        for case in self.__case_list:
            if case.position == position:
                return case
        return None


