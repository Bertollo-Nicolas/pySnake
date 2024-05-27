import pygame
import random
from typing import List
from pygame import Surface
from config.settings import CELL_SIZE

class GridObject:
    def __init__(self, grid: List[List[int]], color: tuple, value: int) -> None:
        self.grid = grid
        self.grid_display = self.grid.display()
        self.color = color
        self.value = value
        self.position = [0, 0]
        self.set_position()

    def set_position(self) -> None:
        while True:
            rand_row = random.randint(0, 9)
            rand_column = random.randint(0, 9)
            if self.is_valid_position(rand_row, rand_column):
                self.position = [rand_row, rand_column]
                break
            print(f"Position ({rand_row}, {rand_column}) is not valid. Regenerating...")

    def is_valid_position(self, row: int, col: int) -> bool:
        return not self.grid_display[row][col]

    def draw(self, screen: Surface) -> None:
        cell = pygame.Rect(self.position[1] * CELL_SIZE, self.position[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.color, cell)