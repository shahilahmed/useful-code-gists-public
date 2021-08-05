import random
import copy

def abs(x):
	return -x if x <= 0 else x

target = "hello world"

class State:

	def __init__(self,length = 4):
		self.genes = State.genes(length = length)
		
	def deepcopy(self):
		return copy.deepcopy(self)
		
	def evaluate(self):
		result = 0
		for t,v in zip(target,self.genes):
			if t == v:
				result = result + 1
		return (result / len(target))
		
		
	def __str__(self):
		return "{}".format(''.join(self.genes))
	
	def __repr__(self):
		return self.__str__()
		
	@staticmethod
	def gene():
		return random.choice("qwertyuiopasdfghjklzxcvbnm ")
	
	@staticmethod
	def genes(length = 4):
		return [State.gene() for index in range(length)]
		
	@staticmethod
	def new(length = 4):
		return State(length = length)
		
	@staticmethod
	def mutate(state = None):
		other = state.deepcopy()
		index = random.randrange(0,len(state.genes))
		other.genes[index] = State.gene()
		return other
		
	@staticmethod
	def crossover(state = None,other = None):
		that = State.new(length = len(state.genes))
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

def hillclimbing(length = 4,epochs = 100,optimal = 1,size = 100):
	best = State.new(length = length)
	epoch = 1
	while True:
		if epoch >= epochs or State.compare(best.evaluate(),optimal):
			return best
		worst = State.choose(state = best,size = size)
		if State.compare(best.evaluate(),worst.evaluate()):
			continue
		print("Epoch : {:2} Best : {}".format(epoch,best))
		print()
		if State.compare(worst.evaluate(),best.evaluate()):
			best = worst
		epoch = epoch + 1
	return []

def main():
	solution = hillclimbing(length = len(target),epochs = len(target) * 2,optimal = 1,size = 100)
	print("solution: {}".format(solution))
	print()

if __name__ == "__main__":
	main()






