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


mpl.use('Agg')

def fatorial(num):
    i = 1
    n_fat = 1
    while i <= n:
        n_fat = n_fat * i
        i = i + 1
    return n_fat


def geraListaAleatoria(tam):
	lista = []
	while len(lista) < tam:
		n = randint(1,1*tam)
		if n not in lista: lista.append(n)
	return lista

def SelectionSort(vector):
    for i in range(len(vector)):
        min= i
        for j in range(i+1, len(A)):
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

tam_lista = 6
lista = geraListaAleatoria(tam_lista)

for i in fatorial(tam_lista):
    yCaso.append(timeit.timeit('SelectionSort({})'.format(lista),setup="from __main__ import SelectionSort",number=1))


desenhaGrafico(x,yCaso,'Listas','Tempo','Caso')

    
