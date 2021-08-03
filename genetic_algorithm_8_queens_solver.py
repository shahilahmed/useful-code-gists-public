import random

def get_chromosome():
	return random.choice(list(range(8))) ## Any row from 0 to 7

def get_individual():
	return [get_chromosome() for square in range(8)] ## Storing the row number the column array


def fitness(individual):
	result = 0	
	board = [0 for square in range(64)]
	for row,col in zip(individual,range(8)): ## Zip the row and column and setting it on the board
		board[row * 8 + col] = 1
	for row in range(8):
		for col in range(8):
			square = row * 8 + col
			if board[square] == 1:
				for delta_row,delta_col in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					to_row,to_col = row,col
					while True:
						to_row = to_row + delta_row
						to_col = to_col + delta_col
						if to_row >= 0 and to_row <= 7 and to_col >= 0 and to_col <= 7:
							if board[to_row * 8 + to_col] == 1: ## Queen is bieng attacked
								result = result + 1
								break
						else:	
							break				
	return result ## Fitness should be 0 ie No Queen is attacking to the Other Queen
	
def str_individual(individual):
	board = [0 for square in range(64)]
	for row,col in zip(individual,range(8)):
		board[row * 8 + col] = 1	
	str_data = "\nBoard:\n\n"
	for row in range(8):
		for col in range(8):
			square = row * 8 + col
			str_data = str_data + "{} ".format('*' if board[square] == 1 else '.')
		str_data = str_data + '\n'
	str_data = str_data + '\n'
	return str_data

def generate_population(pouplations = 100):
	return [get_individual() for index in range(pouplations)]
	
def crossover(a,b):
	c = []
	for gene_a,gene_b in zip(a,b):
		if random.random() > 0.50:
			c.append(gene_a)
		else:	
			c.append(gene_b)
	if random.random() < 0.10:
		c[random.choice(list(range(len(a))))] = get_chromosome()
	return c
		
def genetic_algorithm(pouplations = 1000,epochs = 1000,verbose = False):
	population = generate_population(pouplations)
	epoch = 1
	found = False
	while epoch <= epochs:
		population = sorted(population,key = lambda x : fitness(x))
		if verbose:
			print("epoch : {} {}\n{} \nfitness: {}".format(epoch,
				population[0],str_individual(population[0]),fitness(population[0])))
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
	solution = genetic_algorithm(pouplations = 1000,epochs = 1000,verbose = True)
	print()
	print("Solution: {}\n{}".format(solution,str_individual(solution)))
	print()

	
if __name__ == "__main__":
	main()
	
