#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:30:13 2019

@author: alunos-lmc04
"""

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

def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    resposta = []
    for i in range(length):
        resposta = resposta + buckets[i]
 
    return resposta
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

        
def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'bucketSort')
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
    yPiorCaso.append(timeit.timeit('bucketSort({})'.format(lista),setup="from __main__ import bucketSort",number=1))
    
    lista = geraListaAleatoria(i)
    yMedioCaso.append(timeit.timeit('bucketSort({})'.format(lista),setup="from __main__ import bucketSort",number=1))
    
    lista = geraListaCresc(i)
    yMelhorCaso.append(timeit.timeit('bucketSort({})'.format(lista),setup="from __main__ import bucketSort",number=1))

desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','Pior_Caso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','Medio_Caso')
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','Melhor_Caso')


for i in listaPermutada:
    tempos.append(timeit.timeit('bucketSort({})'.format(listaPermutada),setup="from __main__ import bucketSort",number=1))
    
maxIdx = tempos.index(max(tempos))

print('Tempo mais demorado:',max(tempos))
print(listaPermutada[maxIdx])  
