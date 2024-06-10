import random
import logging

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()
        self.fitness_values = {id(ind): 0 for ind in self.population}
        logging.info(f"Initialized population with {len(self.population)} individuals")

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = self.random_individual()
            population.append(individual)
        return population

    def random_individual(self):
        moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        individual = [random.choice(moves) for _ in range(100)]  # 100 moves
        return individual

    def evaluate_fitness(self, individual):
        return self.fitness_values.get(id(individual), 0)

    def set_fitness(self, individual, fitness):
        self.fitness_values[id(individual)] = fitness

    def select_parents(self):
        total_fitness = sum(self.evaluate_fitness(ind) for ind in self.population)
        if total_fitness == 0:
            logging.warning("Total fitness is zero, selecting random parents")
            return random.choice(self.population), random.choice(self.population)
        
        def select_one():
            pick = random.uniform(0, total_fitness)
            current = 0
            for individual in self.population:
                current += self.evaluate_fitness(individual)
                if current > pick:
                    return individual
        
        parent1 = select_one()
        parent2 = select_one()
        
        # Ensure two different parents
        while parent2 == parent1:
            parent2 = select_one()
        
        return parent1, parent2

    def crossover(self, parent1, parent2):
        if parent1 is None or parent2 is None:
            logging.error("Crossover called with None parent")
            return self.random_individual(), self.random_individual()
        
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
                individual[i] = random.choice(moves)
        return individual

    def evolve(self):
        logging.info("Evolution started")
        new_population = []
        while len(new_population) < self.population_size:
            parent1, parent2 = self.select_parents()
            logging.info(f"Selected parents with fitness {self.evaluate_fitness(parent1)}, {self.evaluate_fitness(parent2)}")
            child1, child2 = self.crossover(parent1, parent2)
            logging.info(f"Crossover completed: {child1[:5]}..., {child2[:5]}...")
            new_population.append(self.mutate(child1))
            new_population.append(self.mutate(child2))
            logging.info(f"Mutation completed and children added to new population, current size: {len(new_population)}")
        self.population = new_population[:self.population_size]
        self.fitness_values = {id(ind): 0 for ind in self.population}
        logging.info(f"Evolved to new population with {len(self.population)} individuals")
