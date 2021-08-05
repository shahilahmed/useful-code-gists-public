import random
import copy

def abs(x):
	return -x if x <= 0 else x

def func(x,y):
	result = (2 * x + 3 * y)
	return result

class State:

	def __init__(self):
		self.genes = State.genes(2)
		
	def deepcopy(self):
		return copy.deepcopy(self)
		
	def evaluate(self):
		x,y = self.genes
		return (1 / (1 + abs(30 - func(x,y))))
		
	def __str__(self):
		x,y = self.genes
		return "2 * {:2} + 3 * {:2} = {:2} Evaluate: {}".format(x,y,func(x,y),self.evaluate())
	
	def __repr__(self):
		return self.__str__()
		
	@staticmethod
	def gene():
		return random.randint(1,10)
	
	@staticmethod
	def genes(length = 4):
		return [State.gene() for index in range(length)]
		
	@staticmethod
	def new():
		return State()
		
	@staticmethod
	def mutate(state = None):
		other = state.deepcopy()
		index = random.randrange(0,len(state.genes))
		other.genes[index] = other.genes[index] + 1 if random.random() > 0.50 else other.genes[index] - 1 
		return other
		
	@staticmethod
	def crossover(state = None,other = None):
		that = State.new()
		for index in range(len(that.genes)):
			if random.random() > 0.50:
				that.genes[index] = state.genes[index]
			else:
				that.genes[index] = other.genes[index]
		return that
		
	@staticmethod
	def next(state = None,other = None):
		that = State.crossover(state = state,other = other)
		if random.random() < 0.15:
			that = State.mutate(that)
		return that
	
	@staticmethod
	def choose(state = None,size = 100):
		states = [State.mutate(state = state) for index in range(size)]
		others = [State.mutate(state = random.choice(states)) for index in range(size)]
		thats = []
		for s,o in zip(states,others):
			thats.append(State.next(state = s,other = o))
		thats = sorted(thats,key = lambda x: x.evaluate(),reverse = True)
		return thats[0]
		
	@staticmethod
	def compare(self,other):
		return self >= other

def hillclimbing(epochs = 100,optimal = 1,size = 100):
	best = State.new()
	epoch = 1
	while True:
		if epoch >= epochs or State.compare(best.evaluate(),optimal):
			return best
		worst = State.choose(state = best,size = size)
		if State.compare(best.evaluate(),worst.evaluate()):
			continue
		print("Epoch : {} Best : {}".format(epoch,best))
		if State.compare(worst.evaluate(),best.evaluate()):
			best = worst
		epoch = epoch + 1
	return []

def main():
	solution = hillclimbing(epochs = 10,optimal = 1,size = 100)
	print(solution)

if __name__ == "__main__":
	main()






