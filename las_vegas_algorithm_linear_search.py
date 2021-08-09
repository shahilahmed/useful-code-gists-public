import random

n = 100

def lvs(arr = [],key = 0):
	counter = 1
	found = False
	while not found:
		index = random.choice(list(range(n)))
		print("Counter : {} key : {} value : {}".format(counter,key,arr[index]))
		if arr[index] == key:
			found = True
		counter = counter + 1
	
arr = list(range(n))
random.shuffle(arr)
lvs(arr,random.choice(arr))
