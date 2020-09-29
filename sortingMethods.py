import sys


def insertion(data, compare, counter):
    for i in range(1, len(data)):
        j = i - 1
        aux = data[i]
        while (j >= 0) and compare(aux, data[j], counter):
            data[j + 1] = data[j]
            counter['movements'] += 1
            j -= 1
        data[j + 1] = aux


def selection(data, compare, counter):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if not compare(data[min_idx], data[j], counter):
                min_idx = j
                counter['movements'] += 1
        data[i], data[min_idx] = data[min_idx], data[i]


def quick(lista, compare, counter, start=0, end=None):
    sys.setrecursionlimit(10 ** 6)
    if end is None:
        end = len(lista) - 1
    if end > start:
        p = partition(lista, start, end, counter, compare)
        # recursivamente na sublista à esquerda (menores)
        quick(lista, compare, counter, start, p - 1)
        # recursivamente na sublista à direita (maiores)
        quick(lista, compare, counter, p + 1, end)


def partition(lista, start, end, counter, compare):
    pivot = lista[start]
    left = start + 1
    right = end
    while left < right:
        while left <= end and compare(lista[left], pivot, counter, True):
            left += 1
        while right > start and not compare(lista[right], pivot, counter):
            right -= 1
        if left < right:
            counter['comparisons'] += 1
            counter['movements'] += 1
            lista[left], lista[right] = lista[right], lista[left]
    counter['movements'] += 1
    lista[start], lista[right] = lista[right], pivot
    return right


def merge(alist, compare, counter):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge(lefthalf, compare, counter)
        merge(righthalf, compare, counter)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if compare(lefthalf[i], righthalf[j], counter):
                alist[k] = lefthalf[i]
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
