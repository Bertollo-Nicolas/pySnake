from typing import List
from config.settings import COLOR_ORANGE_RED
from utils.gridObject import GridObject

class Fruit(GridObject):
    def __init__(self, grid: List[List[int]]) -> None:
        super().__init__(grid, COLOR_ORANGE_RED, 2)