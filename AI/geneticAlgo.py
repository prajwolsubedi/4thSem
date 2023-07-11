import random

# Genetic Algorithm class
class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, fitness_function, crossover_rate=0.8, mutation_rate=0.1):
        self.population_size = population_size
        self.gene_length = gene_length
        self.fitness_function = fitness_function
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            individual = [random.choice([0, 1]) for _ in range(self.gene_length)]
            population.append(individual)
        return population

    def evaluate_fitness(self):
        fitness_scores = []
        for individual in self.population:
            fitness = self.fitness_function(individual)
            fitness_scores.append(fitness)
        return fitness_scores

    def selection(self, fitness_scores):
        total_fitness = sum(fitness_scores)
        probabilities = [fitness / total_fitness for fitness in fitness_scores]
        selected_indices = random.choices(range(self.population_size), probabilities, k=self.population_size)
        selected_population = [self.population[index] for index in selected_indices]
        return selected_population

    def crossover(self, parents):
        children = []
        for i in range(0, len(parents), 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            if random.random() < self.crossover_rate:
                crossover_point = random.randint(1, self.gene_length-1)
                child1 = parent1[:crossover_point] + parent2[crossover_point:]
                child2 = parent2[:crossover_point] + parent1[crossover_point:]
                children.extend([child1, child2])
            else:
                children.extend([parent1, parent2])
        return children

    def mutation(self, population):
        for i in range(len(population)):
            individual = population[i]
            for j in range(len(individual)):
                if random.random() < self.mutation_rate:
                    individual[j] = 1 - individual[j]
            population[i] = individual
        return population

    def evolve(self, num_generations):
        for generation in range(num_generations):
            fitness_scores = self.evaluate_fitness()
            selected_population = self.selection(fitness_scores)
            new_population = self.crossover(selected_population)
            mutated_population = self.mutation(new_population)
            self.population = mutated_population

            best_individual = max(self.population, key=self.fitness_function)
            best_fitness = self.fitness_function(best_individual)
            print(f"Generation: {generation+1} | Best Fitness: {best_fitness} | Best Individual: {best_individual}")


# Example usage:

# Fitness function - maximize the number of ones in the individual
def fitness_function(individual):
    return sum(individual)

# Create a genetic algorithm instance with population size of 100, gene length of 10
ga = GeneticAlgorithm(population_size=100, gene_length=10, fitness_function=fitness_function)

# Evolve the population for 50 generations
ga.evolve(num_generations=50)
