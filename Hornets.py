import numpy as np
import random as rn

#We make the hornet nests [x, y, n]
A = []
A.append([25, 65, 100])
A.append([23, 8, 200])
A.append([7, 13, 327])
A.append([95, 53, 440])
A.append([3, 3, 450])
A.append([54, 56, 639])
A.append([67, 78, 650])
A.append([32, 4, 678])
A.append([24, 76, 750])
A.append([66, 89, 801])
A.append([84, 4, 945])
A.append([34, 23, 967])
#Through calculations we find that the maximum distance between them is (3,3) and (66,89):
dmax = 106.61

#Defining the function that calculates kills
def Kills(Bomb):
    total_kills = 0
    remaining_nests = [nest[:] for nest in A]

    for i in range(12):
        n = A[i][2]
        if n >0:
            d = np.sqrt((Bomb[0] - remaining_nests[i][0])**2 + (Bomb[1] - remaining_nests[i][1])**2)
            kills = n * dmax / (20 * d + 0.00001)
            actual_kills = min(kills, remaining_nests[i][2])
            total_kills += actual_kills
            remaining_nests[i][2] -= np.round(actual_kills)
    return np.round(total_kills)

#Genetic Algorithm parameters
population_size = 50
generations = 100
mutation_rate = 0.1

#Initialize the population with random bomb positions
def initialize_population(size):
    return [[
        [rn.randint(0, 101), rn.randint(0, 101)],
        [rn.randint(0, 101), rn.randint(0, 101)],
        [rn.randint(0, 101), rn.randint(0, 101)]
    ] for _ in range(size)]

#Evaluate the fitness of an individual
def fitness(individual):
    return Kills(individual[0]) + Kills(individual[1]) + Kills(individual[2])

#Select parents based on fitness
def select_parents(population):
    population = sorted(population, key=fitness, reverse=True)
    return population[:len(population)//2]

#Crossover to create children
def crossover(parent1, parent2):
    child = parent1[:]
    for i in range(3):
        if rn.random() > 0.5:
            child[i] = parent2[i][:]
    return child

#Mutation to maintain genetic diversity
def mutate(individual):
    for i in range(3):
        if rn.random() < mutation_rate:
            individual[i] = [rn.randint(0, 101), rn.randint(0, 101)]

#Main genetic algorithm loop
def genetic_algorithm():
    population = initialize_population(population_size)
    
    for generation in range(generations):
        parents = select_parents(population)
        next_population = parents[:]
        
        while len(next_population) < population_size:
            parent1, parent2 = rn.sample(parents, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            next_population.append(child)
        
        population = next_population
    
    best_solution = max(population, key=fitness)
    return best_solution, fitness(best_solution)

#Run the genetic algorithm
best_solution, best_fitness = genetic_algorithm()
print(f"Best bomb positions: {best_solution}")
print(f"Maximum hornets killed: {best_fitness}")
