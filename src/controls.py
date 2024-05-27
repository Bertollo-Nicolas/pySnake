import pygame

def handle_events(game) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.snake.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                game.snake.direction = 'RIGHT'
            elif event.key == pygame.K_UP:
                game.snake.direction = 'UP'
            elif event.key == pygame.K_DOWN:
                game.snake.direction = 'DOWN'
    return True
