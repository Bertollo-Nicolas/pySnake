import pygame
from pygame import Surface
from config.settings import GRID_ROWS
from src.grid import Grid
from src.fruit import Fruit
from src.snake import Snake
import logging

class Game:
    def __init__(self, screen: Surface) -> None:
        self.screen = screen
        self.grid = Grid(GRID_ROWS)
        self.snake = Snake(self.grid)
        self.fruit = Fruit(self.grid)
        self.generate_new_fruit()
        self.game_is_over = False
        logging.info("Game initialized")

    def generate_new_fruit(self):
        self.fruit.set_position()
        self.snake.set_fruit_position(self.fruit.position)
        logging.info(f"New fruit generated at {self.fruit.position}")

    def update(self, move=None):
        if move:
            self.snake.direction = move
            self.snake.update(self.screen)
            self.snake.set_fruit_position(self.fruit.position)
            if self.snake.fruit_eaten:
                self.generate_new_fruit()
                self.snake.fruit_eaten = False
                logging.info(f"Fruit eaten, score: {self.snake.point}")
            if self.snake.game_state:
                self.game_is_over = True
                self.game_over()
                logging.info("Game over triggered")

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
        logging.info(f"Game Over screen displayed with score {self.snake.point}")
        pygame.time.wait(2000)  # Wait for 2 seconds before continuing

    def get_score(self):
        return self.snake.point
