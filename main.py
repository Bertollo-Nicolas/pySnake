import pygame
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, COLOR_BLACK
from src.game import Game
from src.controls import handle_events

# pygame setup
pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()
running = True

game = Game(screen)

while running:
    screen.fill(COLOR_BLACK)

    if not handle_events(game):
        running = False
    game.update()  # Ensure the game update method is called to update snake position
    game.draw()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
