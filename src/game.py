import pygame
from pygame import Surface
from config.settings import GRID_ROWS
from src.grid import Grid
from src.fruit import Fruit
from src.snake import Snake

class Game:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.grid = Grid(GRID_ROWS)
        self.snake = Snake(self.grid)
        self.fruit = Fruit(self.grid)
        self.generate_new_fruit()

    def generate_new_fruit(self):
        self.fruit.set_position()
        self.snake.set_fruit_position(self.fruit.position)

    def update(self) -> None:
        self.snake.update(self.screen)
        self.snake.set_fruit_position(self.fruit.position)
        if self.snake.fruit_eaten:
            self.generate_new_fruit()
            self.snake.fruit_eaten = False
        if self.snake.game_state:
             self.game_over()

    def draw(self) -> None:
        self.grid.draw(self.screen)
        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)

    def game_over(self) -> None:
            font = pygame.font.SysFont(None, 55)
            game_over_surface = font.render(f'Game Over: {self.snake.point}', True, (255, 0, 0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
            self.screen.blit(game_over_surface, game_over_rect)
            pygame.display.update()