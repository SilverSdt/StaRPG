from __future__ import annotations

class Animation:

    def __init__(self: Animation, initial_stance: tuple[int, int, int, int], animation_loop: list[tuple[int, int, int, int, int]], trigger: int) -> None:
        self.initial_stance: tuple[int, int , int, int] = initial_stance
        self.animation_loop: list[tuple[int, int , int, int, int]] = animation_loop.copy()
        self.trigger: int | None = trigger
        self.state: bool = True
        self.tick: int = 0

        self.index: int = 0

    def __next__(self: Animation) -> tuple[int, int, int, int]:
        if self.animation_loop != []:
            res: tuple[int, int, int, int] = self.animation_loop[self.index][:4]
            old_index: int = self.index

            if self.tick == self.animation_loop[self.index][-1]:
                self.index = (self.index + 1) % len(self.animation_loop)


            if self.index == old_index: self.tick += 1
            else: self.tick = 0
        else:
            res: tuple[int, int, int, int] = self.initial_stance
            self.tick = 0

        return res