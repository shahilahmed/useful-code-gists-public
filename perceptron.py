import random
import math
##random.seed(0)

activation_function = "relu"

activation_functions = {
	"sigmoid" : {
		"func" : lambda x : (1 / (1 + math.exp(-x) )),
		"dfunc" : lambda y : (y * (1 - y))
	},
	"tanh" : {
		"func" : lambda x : (math.tanh(x)),
		"dfunc" :  lambda y : (1 - (y * y))
	},
	"relu" : {
		"func" :  lambda x : ( x if x >= 0 else 0),
		"dfunc" : lambda y : ( 1 if y >= 0 else 0)
	}
}

def func(x):
	return activation_functions[activation_function]["func"](x)

def dfunc(y):
	return activation_functions[activation_function]["dfunc"](y)

def predict(layers_i = [],weights = []):
	return func(sum(list(map(lambda x : x[0] * x[1],list(zip(layers_i + [1],weights))))))
	
def train(datasets = [],epochs = 10000,step = 0.1,verbose = False):
	delta = int(epochs * 0.05)
	nodes = len(datasets[0][0])
	weights = [(random.random() - 0.5) for node in range(nodes)]
	weights.append(random.random() - 0.5)
	epoch = 1
	while epoch <= epochs:
		dataset = random.choice(datasets)
		layers_i = dataset[0]
		target = dataset[1]
		output = predict(layers_i + [1],weights)
		error = (target - output)
		gradient = error * step * dfunc(output)
		weights = list(map(lambda x : x[1] + x[0] * gradient,list(zip(layers_i + [1],weights))))
		if verbose:
			if epoch % delta == 0:
				print("{:3}% Completed Error: {}".format(int(epoch * 100 / epochs),error))
		epoch = epoch + 1
	return weights
	
def test(datasets = [],weights = [],verbose = False):
	correct = 0
	for dataset in datasets:
		layers_i = dataset[0]
		target = dataset[1]
		output = predict(layers_i,weights)
		if round(output) == target:
			correct = correct + 1
		if verbose:
			print("layers_i: {} target: {} output: {}".format(layers_i,target,output))
	accuracy = ((correct / len(datasets) ) * 100)
	error = (100 - accuracy)
	return (accuracy,error)

def nand():
	global activation_function 
	activation_function = "sigmoid"
	ds_train = [
		[[0,0,0],1],
		[[0,0,1],0],
		[[0,1,0],0],
		[[1,0,0],0],
		[[1,1,1],0]
	]
	ds_test = [
		[[0,0,0],1],
		[[0,0,1],0],
		[[0,1,0],0],
		[[0,1,1],0],
		[[1,0,0],0],
		[[1,0,1],0],
		[[1,1,0],0],
		[[1,1,1],0]
	]
	weights = train(datasets = ds_train,epochs = 10000,step = 0.1,verbose = False)
	accuracy,error = test(datasets = ds_test,weights = weights,verbose = False)
	print("weights: {}".format(weights))
	print("accuracy: {}% error: {}%".format(accuracy,error))

def equation(f):
	global activation_function
	activation_function = "relu"
	ds_train = [
		[[1],f(1)],
		[[2],f(2)],
		[[3],f(3)],
		[[4],f(4)],
		[[5],f(5)]
	]
	ds_test = []
	numbers = list(range(50))
	for count in range(10):
		x = random.choice(numbers)
		y = f(x)
		ds_test.append([[x],y])
	weights = train(datasets = ds_train,epochs = 10000,step = 0.1,verbose = False)
	accuracy,error = test(datasets = ds_test,weights = weights,verbose = True)
	print("weights: {}".format(weights))
	print("accuracy: {}% error: {}%".format(accuracy,error))	

def main():
	nand()
	##equation(lambda x : 2 * x + 3)
	equation(lambda x : x * 2)
	

if __name__ == "__main__":
	main()
