from main import *
from sortingMethods import *

alredy_sorted = ['abacaxi', 'banana', 'limao', 'maça', 'morando', 'uva']
inversed = ['uva', 'morando', 'maça', 'limao', 'banana', 'abacaxi']
repeated = ['abacaxi', 'banana', 'limao', 'banana', 'morando', 'limao']
repeated_sorted = ['abacaxi', 'banana', 'banana', 'limao', 'limao', 'morando']


def test_merge_list_ordened():
    order = merge(alredy_sorted, compare)
    print(order)
    assert order['data'] == alredy_sorted


def test_merge_list_inversed():
    assert merge(inversed, compare)['data'] == alredy_sorted


def test_merge_list_repeated():
    assert merge(repeated, compare)['data'] == repeated_sorted
