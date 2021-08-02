def func(x):
	return x

def dfunc(y):
	return 1

def predict(x = 0,m = 0,c = 0):
	return func(x * m + c)
	
def learn(x = 0,target = 0,m = 0,c = 0,step = 0.1):
	output = predict(x,m,c)
	error = target - output
	gradient = step * error * dfunc(output)
	m = m + gradient * x
	c = c + gradient
	return m,c
	
def train(epochs = 20,datasets = []):
	m = 0
	c = 0
	index = 1
	while index <= epochs:
		for dataset in datasets:
			x = dataset[0]
			target = dataset[1]
			m,c = learn(x,target,m,c)
			index = index + 1
	return m,c
	
def main():
	datasets = [
		[1,9 * 1 + 6],
		[2,9 * 2 + 6],
		[3,9 * 3 + 6],
		[4,9 * 4 + 6],
		[5,9 * 5 + 6]
	]
	m,c = train(epochs = 10000,datasets = datasets)
	print("m: {} c: {}".format(round(m),round(c)))
	print("m: {} c: {}".format(m,c))
	print()
	for dataset in datasets:
		x = dataset[0]
		target = dataset[1]
		output = predict(x = x,m = m,c = c)
		print("x : {} output : {} target : {} - {}".format(x,output,target,round(output)))
	print()


if __name__ == "__main__":
	main()






