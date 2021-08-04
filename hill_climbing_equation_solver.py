import random

def abs(x):
	return x if x >= 0 else -x

def get_gene():
	return random.randint(-10,10)

def generate():
	return [get_gene() for index in range(4)]

	
def func(state):
	result = 0
	result = result + 1 * state[0]
	result = result + 1 * state[1]
	result = result + 1 * state[2]
	result = result + 1 * state[3]
	return result
	
def evaluate(state):
	return abs(0 - func(state))

def str_state(state):
	str_data = "{:3} + {:3} + {:3} + {:3} = {:3}".format(
		state[0],state[1],state[2],state[3],func(state))
	return str_data
	
def mutate(state):
	new_state = []
	rand_index = random.choice(list(range(len(state))))
	for index in range(len(state)):
		if index == rand_index:
			new_state.append(get_gene())
		else:
			new_state.append(state[index])
	'''
	for index in range(len(state)):
		if random.random() > 0.70:
			new_state[index] = get_gene()
	'''
	return new_state
	
def choose(current_state):	
	states = [mutate(current_state) for index in range(1000)]
	states = sorted(states,key = lambda x : evaluate(x))
	new_state = states[0]
	return new_state
	
def hill_climbing():
	current_state = generate()
	epoch = 1
	epochs = 1000
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





