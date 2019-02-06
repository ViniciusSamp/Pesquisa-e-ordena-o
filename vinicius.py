from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def geraLista(tam):
	lista = []
	for i in range(tam):
		n = randint(1,1*tam)
		if n not in lista: lista.append(n)
	return lista

mpl.use('Agg')

def bubbleSort(vector):
	count = 0
	length = len(vector)
	for i in range(length):
		for j in range(length - i - 1):
			count+=1
			if vector[j] > vector[j+1]:
				vector[j], vector[j+1] = vector[j+1], vector[j]
	return count

def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'bubbleSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)

x = [10000,20000,30000,40000,50000]
y = []

swaps = []

for i in range(5):
	lista = geraLista(x[i])
	swaps.append(bubbleSort(lista))
	y.append(timeit.timeit('bubbleSort({})'.format(lista),setup="from __main__ import bubbleSort",number=1))

desenhaGrafico(x, y, "Quantity", "Time","grafico_bolha")
desenhaGrafico(x, swaps, "Quantity", "Compars", "grafico_compars")
print(swaps)
