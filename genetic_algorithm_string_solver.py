import random

target = "Md Shahil Ahmed"

def func(individual):
	result = 0
	for a,b in zip(list(target),individual):
		if a == b:
			result = result + 1
	return result

def fitness(individual):
	return (len(target) - func(individual))
	
def get_chromosome():
	chars = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM "
	return random.choice(chars)
	
def	str_chromosome(individual):
	str_data = ''.join(individual)
	return str_data
	
def get_individual(n = len(target)):
	return [get_chromosome() for index in range(n)]

def generate_population(pouplations = 100):
	return [get_individual() for index in range(pouplations)]
	
def crossover(a,b):
	c = []
	for gene_a,gene_b in zip(a,b):
		if random.random() > 0.80:
			c.append(gene_a)
		else:	
			c.append(gene_b)
	if random.random() < 0.10:
		c[random.choice(list(range(len(a))))] = get_chromosome()
	return c
	
def genetic_algorithm(pouplations = 1000,epochs = 1000):
	population = generate_population(pouplations)
	epoch = 1
	found = False
	while epoch <= epochs:
		population = sorted(population,key = lambda x : fitness(x))
		print("epoch : {} {} func : {} fitness: {}".format(epoch,
			str_chromosome(population[0]),func(population[0]),fitness(population[0])))
		if fitness(population[0]) == 0:
			found = True
			break
		x = int(len(population) * 0.10)
		y = len(population) - x
		new_population = []
		for index in range(x):
			new_population.append(population.pop(0))
		for index in range(y):
			a = random.choice(new_population)
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
	solution = genetic_algorithm(pouplations = 1000,epochs = 1000 * 10)
	print()
	print("Solution: {}".format(str_chromosome(solution)))
	print()

	
if __name__ == "__main__":
	main()
