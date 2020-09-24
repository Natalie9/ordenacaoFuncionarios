import argparse

from sortingMethods import *


def readCsv(path):
    print(path)
    arr = []
    with open(path) as f:
        for line in f:
            arr.append(line)
    return arr


def compare(a, b):
    '''
        compara se a < b
    '''
    return a.split(',')[0] < b.split(',')[0]


def parseSortingMethod(arg, data):
    switcher = {
        'insertion': insertion,
        'selection': selection,
        'merge': mergeSort,
        'quick': quick,
    }
    # Get the function from switcher dictionary
    func = switcher.get(arg, lambda: "Invalid method")
    # Execute the function
    return func(data, compare)


def writeResult(data):
    with open('result.txt', 'w') as f:
        f.writelines(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str, default='docs/5000/random.csv')
    parser.add_argument('-m', type=str, default='insertion', help="['insertion', 'selection', 'merge' ,'quick']")
    args = parser.parse_args()

    print("reading data...")
    data = readCsv(args.f)

    print("sorting...")

    g = parseSortingMethod(args.m, data)

    writeResult(data)
    print(args.m)
    print('Número de comparações', g['counter']['comparisons'])
    print('Número de movimentações', g['counter']['movements'])
    print('Tempo total', g['total'])
