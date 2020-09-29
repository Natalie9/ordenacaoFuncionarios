from main import *
from sortingMethods import *
import matplotlib.pyplot as plt

from main import sorting

method = 'merge'

alredy_sorted = ['abacaxi', 'banana', 'limao', 'maça', 'morando', 'uva']
inversed = ['uva', 'morando', 'maça', 'limao', 'banana', 'abacaxi']
repeated = ['abacaxi', 'banana', 'limao', 'banana', 'morando', 'limao']
repeated_sorted = ['abacaxi', 'banana', 'banana', 'limao', 'limao', 'morando']


# def test_merge_list_ordened():
#     order = merge(alredy_sorted, compare)
#     print(order)
#     assert order['data'] == alredy_sorted
#
#
# def test_merge_list_inversed():
#     assert merge(inversed, compare)['data'] == alredy_sorted
#
#
# def test_merge_list_repeated():
#     assert merge(repeated, compare)['data'] == repeated_sorted


def test_merge_1000():
    file = '../docs/1000/crescente.csv'
    crescente = sorting(file, method, alredy_sorted)

    file = '../docs/1000/decrescente.csv'
    decrescente = sorting(file, method, inversed)

    file = '../docs/1000/random.csv'
    random = sorting(file, method, repeated)

    title = method + ' 1000'
    plot_data(crescente, decrescente, random, title)

def plot_data(crescente, decrescente, random, title):
    names = ['crescente', 'decrescente', 'random']

    comparisons = [crescente['counter']['comparisons'], decrescente['counter']['comparisons'],
                   random['counter']['comparisons']]
    movements = [crescente['counter']['movements'], decrescente['counter']['movements'], random['counter']['movements']]
    total = [crescente['total'], decrescente['total'], random['total']]

    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.ylabel('Comparaçoes')
    plt.plot(names, comparisons)

    plt.subplot(132)
    plt.ylabel('Movimentacoes')
    plt.plot(names, movements)

    plt.subplot(133)
    plt.ylabel('Tempo (s)')
    plt.plot(names, total)

    plt.suptitle(title)

    plt.show()