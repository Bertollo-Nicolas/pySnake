import pygame
from typing import List
from config.settings import COLOR_LIME, MOVE_DELAY
from utils.gridObject import GridObject
from pygame import Surface
from config.settings import CELL_SIZE

class Snake(GridObject):
    def __init__(self, grid: List[List[int]]) -> None:
        self.body = []  # Initialize body before calling the parent constructor
        super().__init__(grid, COLOR_LIME, 1)
        self.body = [self.position.copy()]  # Set the initial position of the snake's body
        self.last_move_time = pygame.time.get_ticks()
        self.direction = None
        self.fruit_position = None
        self.screen = None
        self.fruit_eaten = False
        self.game_state = False
        self.point = 0

    def set_fruit_position(self, position) -> None:
        self.fruit_position = position

    def update(self, screen: Surface) -> None:
        self.screen = screen
        current_time = pygame.time.get_ticks()
        if current_time - self.last_move_time > MOVE_DELAY:
            self.update_body()
            self.last_move_time = current_time

    def update_body(self) -> None:
        if self.direction:
            new_head = self.body[0].copy()
            if self.direction == 'LEFT':
                new_head[1] -= 1
            elif self.direction == 'RIGHT':
                new_head[1] += 1
            elif self.direction == 'UP':
                new_head[0] -= 1
            elif self.direction == 'DOWN':
                new_head[0] += 1

            if self.is_valid_position(new_head[0], new_head[1]):
                self.body.insert(0, new_head)
                if self.is_eating_fruit(self.fruit_position):
                    self.fruit_eaten = True
                    self.point += 1
                if not self.is_eating_fruit(self.fruit_position):
                    self.body.pop()

    def move_left(self) -> None:
        self.direction = 'LEFT'

    def move_right(self) -> None:
        self.direction = 'RIGHT'

    def move_up(self) -> None:
        self.direction = 'UP'

    def move_down(self) -> None:
        self.direction = 'DOWN'

    def grow(self) -> None:
        self.body.append(self.body[-1].copy())

    def is_eating_fruit(self, fruit_position) -> bool:
        return self.body[0] == fruit_position

    def is_valid_position(self, row: int, col: int) -> bool:
        # Check if the position is within the grid boundaries
        if 0 <= row < len(self.grid_display) and 0 <= col < len(self.grid_display[0]):
            # Check if the position is not colliding with the snake's body
            for segment in self.body:
                if segment == [row, col]:
                    self.game_state = True
                    return False
            return True
        self.game_state = True
        return False

    def draw(self, screen: Surface) -> None:
        for segment in self.body:
            cell = pygame.Rect(segment[1] * CELL_SIZE, segment[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, self.color, cell)
