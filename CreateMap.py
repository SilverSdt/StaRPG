from engine.Case import Case
from engine.Map import Map

cases: list[Case] = []
for i in range(0, 1920, 64):
    for j in range(0, 1080, 64):
        if (i + j) % 128 == 0:
            cases.append(Case((i, j), (64, 64), (0,0,0), False))

m: Map = Map("test field", cases)