from main import *
from sortingMethods import *

alredy_sorted = ['abacaxi', 'banana', 'limao', 'maça', 'morando', 'uva']
inversed = ['uva', 'morando', 'maça', 'limao', 'banana', 'abacaxi']
repeated = ['abacaxi', 'banana', 'limao', 'banana', 'morando', 'limao']
repeated_sorted = ['abacaxi', 'banana', 'banana', 'limao', 'limao', 'morando']


def test_quick_list_ordened():
    order = quick(alredy_sorted, compare)
    print(alredy_sorted, order['data'])
    print('Número de trocas', order['counter'])
    print('Tempo total', order['total'])
    assert alredy_sorted == order['data']


def test_quick_list_inversed():
    assert quick(inversed, compare)['data'] == alredy_sorted


def test_quick_list_repeated():
    assert quick(repeated, compare)['data'] == repeated_sorted
