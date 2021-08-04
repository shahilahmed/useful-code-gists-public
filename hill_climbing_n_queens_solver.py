import random

n = 8

def abs(x):
	return x if x >= 0 else -x

def get_gene():
	return random.choice(list(range(n)))

def generate():
	return [get_gene() for index in range(n)]

		
def evaluate(state):
	result = 0	
	board = [0 for square in range(n*n)]
	for row,col in zip(state,range(n)): ## Zip the row and column and setting it on the board
		board[row * n + col] = 1
	for row in range(n):
		for col in range(n):
			square = row * n + col
			if board[square] == 1:
				for delta_row,delta_col in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					to_row,to_col = row,col
					while True:
						to_row = to_row + delta_row
						to_col = to_col + delta_col
						if to_row >= 0 and to_row <= n - 1 and to_col >= 0 and to_col <= n - 1:
							if board[to_row * n + to_col] == 1: ## Queen is bieng attacked
								result = result + 1
								break
						else:	
							break				
	return result ## Fitness should be 0 ie No Queen is attacking to the Other Queen

def str_state(state):
	board = [0 for square in range(n*n)]
	for row,col in zip(state,range(n)):
		board[row * n + col] = 1	
	str_data = "\nBoard:\n\n"
	for row in range(n):
		for col in range(n):
			square = row * n + col
			str_data = str_data + "{} ".format('*' if board[square] == 1 else '.')
		str_data = str_data + '\n'
	str_data = str_data + '\n'
	return str_data
	
def mutate(state):
	new_state = []
	rand_index = random.choice(list(range(len(state))))
	for index in range(len(state)):
		if index == rand_index:
			new_state.append(get_gene())
		else:
			new_state.append(state[index])
	for index in range(len(state)):
		if random.random() > 0.80:
			new_state[index] = get_gene()
	return new_state
	
def choose(current_state):	
	states = [mutate(current_state) for index in range(10 * n)]
	states = sorted(states,key = lambda x : evaluate(x))
	new_state = states[0]
	return new_state
	
def hill_climbing():
	current_state = generate()
	epoch = 1
	epochs = 100 * n
	while epoch <= epochs:
		next_state = choose(current_state)
		print("epoch : {:4} current_state : {} evaluate: {}".format(epoch,
			str_state(current_state),evaluate(current_state)))
		if evaluate(current_state) == 0:
			break
		if evaluate(next_state) < evaluate(current_state):
			current_state = next_state
		epoch = epoch + 1

hill_climbing()





