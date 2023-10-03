from __future__ import annotations

from typing import  Any, Callable

from engine.Entity import Entity
import pygame

class Control:

    def __init__(self: Control, entity: Entity, func: Callable, variables: dict[str, Any]) -> None:
        self.func: Callable = func
        self.variables: dict[str, Any] = variables

    def __call__(self: Control ,*args: Any, **kwds: Any) -> Any:
        kwds.update(self.variables)
        return self.func(*args, **kwds)