import pygame
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, COLOR_BLACK
from src.game import Game
from src.controls import handle_events
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm

# pygame setup
pygame.init()
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
clock = pygame.time.Clock()

# Genetic Algorithm setup
population_size = 10
mutation_rate = 0.01
crossover_rate = 0.7
generations = 100
ga = GeneticAlgorithm(population_size, mutation_rate, crossover_rate)

def run_game_with_individual(individual):
    game = Game(screen)
    for move in individual:
        screen.fill(COLOR_BLACK)

        if not handle_events(game):
            break
        game.update(move)  # Update the game state with the current move
        game.draw()
        pygame.display.flip()

        clock.tick(FPS)

        if game.game_is_over:
            break
    
    return game.get_score()  # Return the score as the fitness value

def main():
    best_individual = None
    best_fitness = 0

    for generation in range(generations):
        for individual in ga.population:
            fitness = run_game_with_individual(individual)
            ga.set_fitness(individual, fitness)
        
        best_individual = max(ga.population, key=ga.evaluate_fitness)
        best_fitness = ga.evaluate_fitness(best_individual)
        print(f"Generation {generation}: Best Fitness = {best_fitness}")

        ga.evolve()
    
    # Run the game with the best individual
    run_game_with_individual(best_individual)

    pygame.quit()

if __name__ == "__main__":
    main()
