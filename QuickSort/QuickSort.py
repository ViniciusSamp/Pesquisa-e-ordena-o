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
from random import randrange
sys.setrecursionlimit(1000000)


mpl.use('Agg')

def geraLista(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam -= 1
    return lista


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort(lst, start, end):
    if start >= end:
        return lst
    pivot = randrange(start, end + 1)
    new_pivot = partition(lst, start, end, pivot)
    quick_sort(lst, start, new_pivot - 1)
    quick_sort(lst, new_pivot + 1, end)


def QuickSort(lst):
    quick_sort(lst, 0, len(lst) - 1)
    return lst

lista = geraLista(100000)

print(QuickSort(lista))

def desenhaGrafico(x,y,xl,yl,label):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = 'QuickSort')
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig(label)
    
x = [1000000,2000000,3000000,4000000,5000000]

yCaso = []

for i in x:
    lista = geraLista(i)
    yCaso.append(timeit.timeit('QuickSort({})'.format(lista),setup="from __main__ import QuickSort",number=1))

desenhaGrafico(x,yCaso,'Quantidade','Tempo','Caso')    
