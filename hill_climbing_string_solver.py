import random

target = "hello world"

target = "to be or not to be is the question"

def generate():
	return [random.choice("qwertyuiopasdfghjklzxcvbnm ") for index in range(len(target))]

def evaluate(state):
	result = 0
	for index in range(len(target)):
		if state[index] != target[index]:
			result = result + 1
	return result

def mutate(state):
	new_state = []
	rand_index = random.choice(list(range(len(state))))
	for index in range(len(state)):
		if index == rand_index:
			new_state.append(random.choice("qwertyuiopasdfghjklzxcvbnm "))
		else:
			new_state.append(state[index])
	return new_state
	
def choose(current_state):	
	states = [mutate(current_state) for index in range(100)]
	states = sorted(states,key = lambda x : evaluate(x))
	new_state = states[0]
	return new_state
	
def hill_climbing():
	current_state = generate()
	epoch = 1
	epochs = 10000
	while epoch <= epochs:
		next_state = choose(current_state)
		print("epoch : {:4} current_state : {} evaluate: {}".format(epoch,
			''.join(current_state),evaluate(current_state)))
		if evaluate(current_state) == 0:
			break
		if evaluate(next_state) < evaluate(current_state):
			current_state = next_state
		epoch = epoch + 1

hill_climbing()





