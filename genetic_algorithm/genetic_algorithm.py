# src/genetic_algorithm.py

import random

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()
        self.fitness_values = {id(ind): 0 for ind in self.population}

    def initialize_population(self):
        # Initialize the population with random individuals
        population = []
        for _ in range(self.population_size):
            individual = self.random_individual()
            population.append(individual)
        return population

    def random_individual(self):
        # Example: random snake configuration (this should be adapted to your game's specifics)
        moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        individual = [random.choice(moves) for _ in range(100)]  # 100 moves
        return individual

    def evaluate_fitness(self, individual):
        # Retrieve fitness value from dictionary
        return self.fitness_values[id(individual)]

    def set_fitness(self, individual, fitness):
        # Store fitness value in dictionary
        self.fitness_values[id(individual)] = fitness

    def select_parents(self):
        # Example: roulette wheel selection
        total_fitness = sum(self.evaluate_fitness(ind) for ind in self.population)
        pick = random.uniform(0, total_fitness)
        current = 0
        for individual in self.population:
            current += self.evaluate_fitness(individual)
            if current > pick:
                return individual

    def crossover(self, parent1, parent2):
        # Example: single-point crossover
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        return individual

    def evolve(self):
        # Main loop to evolve the population

        new_population = []

        # Selection
        selected_individuals = [self.select_parents() for _ in range(self.population_size)]

        # Crossover and Mutation
        for i in range(0, self.population_size, 2):
            parent1 = selected_individuals[i]
            parent2 = selected_individuals[i + 1]

            if random.random() < self.crossover_rate:
                child1, child2 = self.crossover(parent1, parent2)
            else:
                child1, child2 = parent1, parent2

            new_population.append(self.mutate(child1))
            new_population.append(self.mutate(child2))

        # Update population
        self.population = new_population
        self.fitness_values = {id(ind): 0 for ind in self.population}
