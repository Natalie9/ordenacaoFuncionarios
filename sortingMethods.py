from datetime import datetime


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


def merge(data, compare):
    pass


def quick(data, compare):
    pass


def mergeSort(alist, compare):
    inicio = datetime.now()
    counter = {'comparisons': 0, 'movements': 0}
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf, compare)
        mergeSort(righthalf, compare)

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
