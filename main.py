import argparse
from datetime import datetime

from sortingMethods import *


def compare(a, b, counter, eq=False):
    '''
        compara se a < b
    '''
    counter['comparisons'] += 1
    if eq:
        return a.split(',')[0] <= b.split(',')[0]
    return a.split(',')[0] < b.split(',')[0]


def parse_sorting_method(arg, data, counter):
    switcher = {
        'insertion': insertion,
        'selection': selection,
        'merge': merge,
        'quick': quick,
    }
    # Get the function from switcher dictionary
    func = switcher.get(arg, lambda: "Invalid method")
    # Execute the function
    return func(data, compare, counter)


def writeResult(data):
    with open('result.txt', 'w') as f:
        f.writelines(data)


def read_csv(path):
    arr = []
    with open(path) as f:
        for line in f:
            arr.append(line)
    return arr


def sorting(file, method):
    data = read_csv(file)
    counter = {'comparisons': 0, 'movements': 0}
    inicio = datetime.now()
    parse_sorting_method(method, data, counter)
    final = datetime.now()
    total = final - inicio
    writeResult(data)
    arq = file.split('docs/')[-1]
    print('\nArquivo {arq} | Algoritmo {alg}'.format(arq=arq, alg=method))
    printing(total, counter)
    return {'counter': counter, 'total': total.total_seconds()}


def printing(total, counter):
    print('Número de comparações', counter['comparisons'])
    print('Número de movimentações', counter['movements'])
    print('Tempo total', total)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='docs/2000/crescente.csv')
    parser.add_argument('-m', type=str, default='merge', help="['insertion', 'selection', 'merge' ,'quick']")
    args = parser.parse_args()

    sorting(args.f, args.m)
    # sorting(alredy_sorted, args.m)
