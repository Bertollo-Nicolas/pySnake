# settings.py
import pygame

# --- Game General Settings ---
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
FPS = 60
MOVE_DELAY = 150

# --- Game Grid Settings ---
GRID_ROWS = 10
GRID_COLUMNS = 10
CELL_SIZE = WINDOW_WIDTH / GRID_ROWS

# --- Game colors Settings ---
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_LIME = pygame.Color(0, 255, 0)
COLOR_ORANGE_RED = pygame.Color(255, 69, 0)
COLOR_DIM_GREY = pygame.Color(105,105,105)