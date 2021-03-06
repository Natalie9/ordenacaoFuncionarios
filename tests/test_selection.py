from main import *
from sortingMethods import *

alredy_sorted = ['abacaxi', 'banana', 'limao', 'maça', 'morando', 'uva']
inversed = ['uva', 'morando', 'maça', 'limao', 'banana', 'abacaxi']
repeated = ['abacaxi', 'banana', 'limao', 'banana', 'morando', 'limao']
repeated_sorted = ['abacaxi', 'banana', 'banana', 'limao', 'limao', 'morando']


def test_selected_list_ordened():
    order = selection(alredy_sorted, compare)
    print('Número de trocas', order['counter'])
    print('Tempo total', order['total'])
    assert alredy_sorted == order['data']


def test_selectedlist_inversed():
    order = selection(inversed, compare)
    print('Número de trocas', order['counter'])
    print('Tempo total', order['total'])
    assert alredy_sorted == order['data']


def test_selected_list_repeated():
    order = selection(repeated, compare)
    print('Número de trocas', order['counter'])
    print('Tempo total', order['total'])
    assert repeated_sorted == order['data']




