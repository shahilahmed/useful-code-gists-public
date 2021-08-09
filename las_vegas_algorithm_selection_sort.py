import math
import random
import copy

def sort(arr = []):
	arr = copy.deepcopy(arr)
	i = 0
	epoch = 1
	while i < len(arr):
		indexes = list(range(i + 1,len(arr)))
		if len(indexes) == 0:
			break
		else:
			while arr[i] != min(arr[i:]):
				j = random.choice(indexes)
				if arr[i] > arr[j]:
					temp = arr[j]
					arr[j] = arr[i]
					arr[i] = temp
			i = i + 1
			print("Epoch : {} arr: {}".format(epoch,arr))
		epoch = epoch + 1
	return arr


def main():
	n = 10
	arr = list(map(lambda x : (x + 1) * random.choice(list(range(1,100))),list(range(n))))
	random.shuffle(arr)
	print(arr)
	arr = sort(arr)
	print(arr)

if __name__ == "__main__":
	main()




