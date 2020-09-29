# ordenacaoFuncionarios
Programa para ordenação das informações de funcionários de uma empresa

# Como executar o programa

 ``python main.py -f [caminho]  -m [metodo]``

Passando o caminho do arquivo que quer ordenar e o método que quer usar para a ordenação. 

Caso nenhum parâmetro seja passado o programa escolherá de forma padrão. 

Para auxílio pode se usar a função ``--help. ``

Os dados ordenados são gravados em um arquivo ``result.txt`` no mesmo diretório de execução. 

## Diretórios

``main.py`` arquivo principal de execução

``sortingMethods.py`` arquivo com implementação dos algoritmos de ordenação 

``/docs ``
  Base de arquivos com dados para ordenação

``/test``
  Testes (pytest) com plotagem de gráficos do desempenho de cada algoritmo 

``/tests ``
  Testes de mesa, com poucos dados para averiguação dos resultados obtidos (necessario connfigurar metodo de leitura do csv)

