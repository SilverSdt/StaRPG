from __future__ import annotations

class Animation:

    def __init__(self: Animation, initial_stance: tuple[int, int, int, int], animation_loop: list[tuple[int, int, int, int]], trigger: int) -> None:
        self.initial_stance: tuple[int, int , int, int] = initial_stance
        self.animation_loop: list[tuple[int, int , int, int]] = animation_loop.copy()
        self.trigger: int | None = trigger
        self.state: bool = True

        self.index: int = 0

    def __next__(self: Animation) -> tuple[int, int, int, int]:
        if self.animation_loop != []:
            res: tuple[int, int, int, int] = self.animation_loop[self.index]
            self.index = (self.index + 1) % len(self.animation_loop)
        else:
            res: tuple[int, int, int, int] = self.initial_stance

        return res