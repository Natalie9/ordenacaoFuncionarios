from datetime import datetime
import sys


def insertion(data, compare):
    inicio = datetime.now()
    counter = {'comparisons': 0, 'movements': 0}
    for i in range(1, len(data)):
        j = i - 1
        aux = data[i]
        counter['comparisons'] += 1
        while (j >= 0) and compare(aux, data[j]):
            data[j + 1] = data[j]
            counter['movements'] += 1
            j -= 1
        data[j + 1] = aux
    fim = datetime.now()
    total = fim - inicio
    return {'data': data, 'counter': counter, 'total': total}


def selection(data, compare):
    inicio = datetime.now()
    counter = {'comparisons': 0, 'movements': 0}
    for i in range(len(data)):
        min_idx = i
        counter['comparisons'] += 1
        for j in range(i + 1, len(data)):
            counter['comparisons'] += 1
            if compare(data[j], data[min_idx]):
                min_idx = j
                counter['movements'] += 1
        data[i], data[min_idx] = data[min_idx], data[i]
    fim = datetime.now()
    total = fim - inicio
    return {'data': data, 'counter': counter, 'total': total}


def quick(lista, compare, start=0, end=None):
    inicio = datetime.now()
    counter = {'comparisons': 0, 'movements': 0}
    if end is None:
        end = len(lista) - 1
    if start < end:
        p = partition(lista, start, end, counter, compare)
        # recursivamente na sublista à esquerda (menores)
        quick(lista, compare, start, p['i'] - 1)
        # recursivamente na sublista à direita (maiores)
        quick(lista, compare, p['i'] + 1, end)
    end = datetime.now()
    total = end - inicio
    return {'data': lista, 'counter': counter, 'total': total}


def partition(lista, start, end, counter, compare):
    pivot = lista[end]
    i = start
    for j in range(start, end):
        # j sempre avança, pois representa o elementa em análise
        # e delimita os elementos maiores que o pivô
        counter['comparisons'] += 1
        if compare(lista[j], pivot):
            lista[j], lista[i] = lista[i], lista[j]
            counter['movements'] += 1
            # incrementa-se o limite dos elementos menores que o pivô
            i = i + 1
    lista[i], lista[end] = lista[end], lista[i]
    return {'counter': counter, 'i': i}


def merge(alist, compare):
    inicio = datetime.now()
    counter = {'comparisons': 0, 'movements': 0}
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge(lefthalf, compare)
        merge(righthalf, compare)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            counter['comparisons'] += 1
            if compare(lefthalf[i], righthalf[j]):
                alist[k] = lefthalf[i]
                counter['movements'] += 1
                i = i + 1
            else:
                alist[k] = righthalf[j]
                counter['movements'] += 1
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

    fim = datetime.now()
    total = fim - inicio
    return {'data': alist, 'counter': counter, 'total': total}


