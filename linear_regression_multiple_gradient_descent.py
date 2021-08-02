def func(x):
	return x

def dfunc(y):
	return 1

def predict(x = 0,weights = [],bias = []):
	hidden = func(weights[0] * x + bias[0])
	output = func(weights[1] * hidden + bias[1])
	return output

def learn(x = 0,target = 0,weights = [],bias = [],step = 0.01):
	hidden = func(weights[0] * x + bias[0])
	output = func(weights[1] * hidden + bias[1])
	error_output = target - output
	error_hidden = weights[1] * error_output
	gradient_output = step * error_output * dfunc(output)
	gradient_hidden = step * error_hidden * dfunc(hidden)
	weights[1] = weights[1] + gradient_output * hidden
	weights[0] = weights[0] + gradient_hidden * x 
	bias[1] = bias[1] + gradient_output
	bias[0] = bias[0] + gradient_hidden
	return weights,bias

def train(epochs = 10000,datasets = [],step = 0.1):
	weights = [1,1]
	bias = [1,1]
	index = 1
	while index <= epochs:
		for dataset in datasets:
			x = dataset[0]
			target = dataset[1]
			m,c = learn(x = x,target = target,weights = weights,bias = bias,step = step)
			index = index + 1
	return weights,bias

def main():
	datasets = [
		[1,9 * 1 + 6],
		[2,9 * 2 + 6],
		[3,9 * 3 + 6],
		[4,9 * 4 + 6],
		[5,9 * 5 + 6]
	]
	weights,bias = train(epochs = 10000,datasets = datasets,step = 0.01)
	print("weights: {} bias: {}".format(weights,bias))
	print()
	for dataset in datasets:
		x = dataset[0]
		target = dataset[1]
		output = predict(x = x,weights = weights,bias = bias)
		print("x : {} output : {} target : {} - {}".format(x,output,target,round(output)))
	print()

if __name__ == "__main__":
	main()













