import random

def abs(x):
	return x if x >= 0 else -x

## bounds : 0 to 30
## solutions: [7,5,3,1],[12, 6, 2, 0],[1,9,1,2],[9,0,7,0],[0,3,0,6,],[10,10,0,0] etc etc
## f(x) = a + 2 * b + 3 * c + 4 * d
## g(x) = abs(30 - f(x))
def func(individual):
	result = 0
	result = result + 1 * individual[0]
	result = result + 2 * individual[1]
	result = result + 3 * individual[2]
	result = result + 4 * individual[3]
	return result

def fitness(individual):
	return abs(30 - func(individual))
	
def get_chromosome(a = 0,b = 30):
	return random.choice(range(a,b + 1))

def get_individual(n = 4):
	return [get_chromosome() for index in range(n)]

def generate_population(pouplations = 100):
	return [get_individual() for index in range(pouplations)]
	
def crossover(a,b):
	c = []
	for gene_a,gene_b in zip(a,b):
		if random.random() > 0.50:
			c.append(gene_a)
		else:	
			c.append(gene_b)
	if random.random() > 0.80:
		c[random.choice(list(range(len(a))))] = get_chromosome()
	return c
	
def genetic_algorithm(pouplations = 1000,epochs = 1000):
	population = generate_population(pouplations)
	epoch = 1
	found = False
	while epoch <= epochs:
		population = sorted(population,key = lambda x : fitness(x))
		print("epoch : {} {} func : {} fitness: {}".format(epoch,
			population[0],func(population[0]),fitness(population[0])))
		if fitness(population[0]) == 0:
			found = True
			break
		x = int(len(population) * 0.10)
		y = len(population) - x
		new_population = []
		for index in range(x):
			new_population.append(population.pop(0))
		for index in range(y):
			a = random.choice(population)
			b = random.choice(population)
			if random.random() < 0.05:
				c = get_individual()
			else:
				c = crossover(a,b)
			new_population.append(c)		
		random.shuffle(new_population)
		population = new_population
		epoch = epoch + 1
	return population[0] if found else []

def main():
	solution = genetic_algorithm(pouplations = 1000,epochs = 10000)
	print(solution)

	
if __name__ == "__main__":
	main()
