import random
import math

def sigmoid(x):
	return (1 / (1 + math.exp(-x) ))  


genes = list(range(1,15))

def create():
	return [random.choice(genes),random.choice(genes)]

def func(arr = []):
	return (2 * arr[0] + 3 * arr[1])
	

def lve():
	found = False
	counter = 1
	while not found:
		arr = create()
		fitness = sigmoid(15 - func(arr))
		if fitness == 0.5:
			found = True
		print("Counter : {:4} Eq : 2*{:2} + 3*{:2} = {:2} fitness : {}".format(
			counter,arr[0],arr[1],func(arr),fitness))
		counter = counter + 1
		
lve()
