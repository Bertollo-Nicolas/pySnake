import pygame
from typing import List
from config.settings import CELL_SIZE, COLOR_DIM_GREY

class Grid:
    def __init__(self, width: int) -> None:
        self.width = width
        self.grid = self.create_grid(self.width)

    def create_grid(self, width: int) -> List[List[int]]:
        return [[0] * width for _ in range(width)]
    
    def display(self) -> List[List[int]]:
        return self.grid

    def draw(self, screen) -> None:
        for row_index, row in enumerate(self.grid):
            for cell_index, cell in enumerate(row):
                if cell == 0:
                    rect = pygame.Rect(cell_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, COLOR_DIM_GREY, rect, width=1)

    def get_value(self, row: int, col: int) -> int:
        if self.is_valid_position(row, col):
            return self.grid[row][col]
        raise IndexError(f"Index out of bounds {row}, {col}")
    
    def set_value(self, row: int, col: int, value: int) -> None:
        if self.is_valid_position(row, col):
            self.grid[row][col] = value
        else:
            raise IndexError(f"Index out of bounds {row}, {col}")
        
    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[row])