import pygame
from config.settings import WINDOW_HEIGHT, WINDOW_WIDTH, FPS, COLOR_BLACK
from src.game import Game
from src.controls import handle_events
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    move_count = 0
    for move in individual:
        if not handle_events():
            logging.info("Game quit by user")
            break
        screen.fill(COLOR_BLACK)
        game.update(move)  # Update the game state with the current move
        game.draw()
        pygame.display.flip()
        clock.tick(FPS)
        move_count += 1
        #logging.info(f"Move {move_count}: {move}, Score: {game.get_score()}, Game Over: {game.game_is_over}")
        if game.game_is_over:
            logging.info("Game over detected")
            break
    return game.get_score()  # Return the score as the fitness value

def main():
    best_individual = None
    best_fitness = 0

    for generation in range(generations):
        logging.info(f"Generation {generation} start")
        for individual in ga.population:
            fitness = run_game_with_individual(individual)
            ga.set_fitness(individual, fitness)
        
        best_individual = max(ga.population, key=ga.evaluate_fitness)
        best_fitness = ga.evaluate_fitness(best_individual)
        logging.info(f"Generation {generation}: Best Fitness = {best_fitness}")
        logging.info(f"Population Fitness: {[ga.evaluate_fitness(ind) for ind in ga.population]}")

        logging.info(f"Generation {generation} evolving")
        ga.evolve()
        logging.info(f"Generation {generation} evolved")
    
    # Run the game with the best individual
    run_game_with_individual(best_individual)
    pygame.quit()

if __name__ == "__main__":
    main()
