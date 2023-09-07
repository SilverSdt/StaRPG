# <========== import ==========>

from __future__ import annotations

from json import load, dump

from engine.Case import Case

# <========== class ==========>

class Map:

    # <----- init ----->

    def __init__(self: Map, name: str, case_list: list[tuple[str, tuple[int, int]]], grid_size: tuple[int, int], screen_size: tuple[int, int] , case_on_screen: tuple[int, int]) -> None:
        self.__name: str = name
        self.__grid_size: tuple[int, int] = grid_size
        self.__screen_size: tuple[int, int] = screen_size
        self.__case_on_screen: tuple[int, int] = case_on_screen
        self.__case_list: list[Case] = []


        for case in case_list:
            with open(f"data/case/{case[0]}.json", "r") as file:
                data: dict = load(file)
                self.__case_list.append(Case(data["name"], data["sprite"], data["hitbox"], (screen_size[0] // case_on_screen[0], screen_size[1] // case_on_screen[1]), (case[1][0] * (screen_size[0] // case_on_screen[0]), case[1][1] * (screen_size[1] // case_on_screen[1]))))


    # <----- getter ----->

    @property
    def name(self: Map) -> str: return self.__name

    @property
    def case_list(self: Map) -> list[Case]: return self.__case_list

    @property
    def grid_size(self: Map) -> tuple[int, int]: return self.__grid_size

    @property
    def screen_size(self: Map) -> tuple[int, int]: return self.__screen_size

    @property
    def case_on_screen(self: Map) -> tuple[int, int]: return self.__case_on_screen

    @property
    def __dict__(self: Map) -> dict[str, object]:
        return {
            "name": self.__name,
            "grid_size": self.__grid_size,
            "case_on_screen": self.__case_on_screen,
            "case_list": [[case.name, [case.position[0] / (self.__screen_size[0] // self.__case_on_screen[0]), case.position[1] / (self.__screen_size[1] // self.__case_on_screen[1])]] for case in self.__case_list]
        }


    # <----- setter ----->

    @name.setter
    def name(self: Map, new_name: str) -> None: self.__name = new_name

    @case_list.setter
    def case_list(self: Map, new_case_list: list[tuple[str, tuple[int, int]]]) -> None:
        self.__case_list = []
        for case in new_case_list:
            with open(f"data/case/{case[0]}.json", "r") as file:
                data: dict = load(file)
                self.__case_list.append(Case(data["name"], data["sprite"], data["hitbox"], (self.__screen_size[0] // self.__case_on_screen[0], self.__screen_size[1] // self.__case_on_screen[1]), (case[1][0] * (self.__screen_size[0] // self.__case_on_screen[0]), case[1][1] * (self.__screen_size[1] // self.__case_on_screen[1]))))

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

    # <----- save ----->

    def save(self: Map) -> None:
        with open(f"data/map/{self.__name}.json", "w+") as file:
            dump(self.__dict__, file)

    # <----- load ----->

    @staticmethod
    def load(map_name: str, screen_size: tuple[int, int]) -> Map:
        with open(f"data/map/{map_name}.json", "r") as file:
            data: dict = load(file)
            return Map(data["name"], [(case[0], case[1]) for case in data["case_list"]], data["grid_size"], screen_size, data["case_on_screen"])