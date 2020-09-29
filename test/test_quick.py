import matplotlib.pyplot as plt

from main import sorting

method = 'quick'


def test_quick():
    file = '../docs/1000/crescente.csv'
    um = sorting(file, method)

    file = '../docs/1000/decrescente.csv'
    deum = sorting(file, method)

    file = '../docs/1000/random.csv'
    raum = sorting(file, method)

    file = '../docs/2000/crescente.csv'
    dois = sorting(file, method)

    file = '../docs/2000/decrescente.csv'
    dedois = sorting(file, method)

    file = '../docs/2000/random.csv'
    radois = sorting(file, method)

    names = ['1000', '2000']

    crescente = [um['counter']['comparisons'], dois['counter']['comparisons']]
    decrescente = [deum['counter']['comparisons'], dedois['counter']['comparisons']]
    random = [raum['counter']['comparisons'], radois['counter']['comparisons']]

    mocrescente = [um['counter']['movements'], dois['counter']['movements']]
    modecrescente = [deum['counter']['movements'], dedois['counter']['movements']]
    morandom = [raum['counter']['movements'], radois['counter']['movements']]

    tecrescente = [um['total'], dois['total']]
    tedecrescente = [deum['total'], dedois['total']]
    terandom = [raum['total'], radois['total']]

    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.ylabel('Comparações')
    plt.plot(names, crescente, label="crescente")
    plt.plot(names, decrescente, label="decrescente")
    plt.plot(names, random, label="random")
    plt.legend()

    plt.subplot(132)
    plt.ylabel('Movimentaçoes')
    plt.plot(names, mocrescente, label="crescente")
    plt.plot(names, modecrescente, label="decrescente")
    plt.plot(names, morandom, label="random")
    plt.legend()

    plt.subplot(133)
    plt.ylabel('Tempo (s)')
    plt.plot(names, tecrescente, label="crescente")
    plt.plot(names, tedecrescente, label="decrescente")
    plt.plot(names, terandom, label="random")
    plt.legend()
    plt.suptitle(method)


def test_quick_1000():
    file = '../docs/1000/crescente.csv'
    crescente = sorting(file, method)

    file = '../docs/1000/decrescente.csv'
    decrescente = sorting(file, method)

    file = '../docs/1000/random.csv'
    random = sorting(file, method)

    title = method + ' 1000'
    plot_data(crescente, decrescente, random, title)


# def test_quick_2000():
#     file = '../docs/2000/crescente.csv'
#     crescente = sorting(file, method)
#
#     file = '../docs/2000/decrescente.csv'
#     decrescente = sorting(file, method)
#
#     file = '../docs/2000/random.csv'
#     random = sorting(file, method)
#
#     title = method + ' 2000'
#     plot_data(crescente, decrescente, random, title)


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
