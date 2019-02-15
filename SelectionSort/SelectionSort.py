#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:49:23 2019

@author: alunos-lmc04
"""

from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
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

def SelectionSort(vector):
    for i in range(len(vector)):
        min= i
        for j in range(i+1, len(vector)):
            if vector[min] > vector[j]:
                min = j
    vector[i], vector[min] = vector[min], vector[i]
    

def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'SelectionSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [1000,2000,3000,4000,5000]

yPiorCaso = []
yMedioCaso = []
yMelhorCaso = []

lista = [1, 2, 3, 4, 5, 6]
listaPermutada = list(it.permutations(lista,6))

tempos = []

for i in x:
    lista = geraListaDecresc(i)
    yPiorCaso.append(timeit.timeit('SelectionSort({})'.format(lista),setup="from __main__ import SelectionSort",number=1))
    
    lista = geraListaAleatoria(i)
    yMedioCaso.append(timeit.timeit('SelectionSort({})'.format(lista),setup="from __main__ import SelectionSort",number=1))
    
    lista = geraListaCresc(i)
    yMelhorCaso.append(timeit.timeit('SelectionSort({})'.format(lista),setup="from __main__ import SelectionSort",number=1))

desenhaGrafico(x,yPiorCaso,'Quantidade','Tempo','Pior_Caso')    
desenhaGrafico(x,yMedioCaso,'Quantidade','Tempo','Medio_Caso')
desenhaGrafico(x,yMelhorCaso,'Quantidade','Tempo','Melhor_Caso')


for i in listaPermutada:
    tempos.append(timeit.timeit('SelectionSort({})'.format(listaPermutada),setup="from __main__ import SelectionSort",number=1))
    
maxIdx = tempos.index(max(tempos))

print('Tempo mais demorado:',max(tempos))
print(listaPermutada[maxIdx])    
