def bubbleSort(vector):
	count = 0
	length = len(vector)
	for i in range(length):
		for j in range(length - i - 1):
			count+=1
			if vector[j] > vector[j+1]:
				vector[j], vector[j+1] = vector[j+1], vector[j]
	return count
