from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it

mpl.use('Agg')

def geraListaAleatoria(tam):
	lista = []
	while len(lista) < tam:
		n = randint(1,1*tam)
		if n not in lista: lista.append(n)
	return lista

def geraListaCresc(tam):
    lista = []
    i = 0
    while i <= tam:
        lista.append(i)
        i+=1
    return lista

def geraListaDecresc(tam):
    lista = []
    while tam >= 0:
        lista.append(tam)
        tam-=1
    return lista

def shellSort(arr): 
  
    # Start with a big gap, then reduce the gap 
    n = len(arr) 
    gap = n//2
  
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array 
    # is gap sorted 
    while gap > 0: 
  
        for i in range(gap,n): 
  
            # add a[i] to the elements that have been gap sorted 
            # save a[i] in temp and make a hole at position i 
            temp = arr[i] 
  
            # shift earlier gap-sorted elements up until the correct 
            # location for a[i] is found 
            j = i 
            while  j >= gap and arr[j-gap] >temp: 
                arr[j] = arr[j-gap] 
                j -= gap 
  
            # put temp (the original a[i]) in its correct location 
            arr[j] = temp 
        gap //= 2
        
        
def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'shellSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [10000,20000,30000,40000,50000]

yPiorCaso = []
yMedioCaso = []
yMelhorCaso = []

lista = [1, 2, 3, 4, 5, 6]
listaPermutada = list(it.permutations(lista,6))

tempos = []

for i in x:
    lista = geraListaDecresc(i)
    yPiorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaAleatoria(i)
    yMedioCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))
    
    lista = geraListaCresc(i)
    yMelhorCaso.append(timeit.timeit('shellSort({})'.format(lista),setup="from __main__ import shellSort",number=1))

desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','Pior_Caso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','Medio_Caso')
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','Melhor_Caso')


for i in listaPermutada:
    tempos.append(timeit.timeit('shellSort({})'.format(listaPermutada),setup="from __main__ import shellSort",number=1))
    
maxIdx = tempos.index(max(tempos))

print('Tempo mais demorado:',max(tempos))
print(listaPermutada[maxIdx])  
