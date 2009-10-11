#!/usr/bin/env python
# coding: utf-8

# INSTRUÇÕES:
#
# - resolva os exercícios colocando suas respostas no lugar dos XXX
#
# - o XXX pode aparecer na linha de entrada (>>>) ou na saída
#
# - siga a ordem, pois em geral os primeiros são mais fáceis
#
# - se você executar os testes, o doctest vai entregar muitas respostas ao 
#   exibir a linha de saída esperada para cada teste; portanto deixe para 
#   executar depois de ter respondido a maioria dos testes
#
# - os XXX nas linhas de entrada são um desafio maior, porque o doctest
#   não vai entregar a resposta, e muitas vezes existem várias respostas
#   possíveis que produzem a mesma saída; procure fornecer a resposta mais
#   simples que satisfaça o exemplo
#
# - a opção REPORT_ONLY_FIRST_FAILURE faz aparecer apenas o primeiro 
#   exercício não resolvido no relatório de testes
#
# - se quiser deixar um exercício para depois, coloque o comentário 
#   "# doctest: +SKIP" na linha de entrada, por exemplo:
#
#   >>> 2 ** 100 # doctest: +SKIP
#   XXX

'''
1. Operações com sequências
-----------------------------

Para estes exercícios, usaremos este exemplo de sequências::

    >>> ufs = {'RJ':'Rio de Janeiro', 'AM':'Amazonas', 'SC':'Santa Catarina'}
    >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5), acel=(0,2,-1), comb=97)
    >>> type(ufs), type(nave)
    (<type 'dict'>, <type 'dict'>)
    
1.1. Acessando elementos::

    >>> ufs['AM']
    'Amazonas'
    >>> ufs['PE']
    Traceback (most recent call last):
    KeyError: 'PE'
    >>> ufs['am']
    Traceback (most recent call last):
    KeyError: 'am'
    >>> sigla = 'rj'
    >>> ufs[sigla.upper()]
    'Rio de Janeiro'    
    >>> nave['vel']
    (0, -5, -5)
    >>> x, y, z = nave['pos']
    >>> z
    9
    >>> nave['acel'][2]
    -1
    >>> ufs.get('SC')
    'Santa Catarina'
    >>> ufs.get('VA','(UF inexistente)')
    '(UF inexistente)'
    >>> ufs.get('SP') is None
    True

1.2. Operações envolvendo o dicionário como um todo

    >>> len(ufs)
    3
    >>> 'sc' in ufs
    False
    >>> 'RJ' in ufs
    True
    >>> 'Amazonas' in ufs
    False
    
A seguir usamos `sorted` para fazer testes reproduzíveis, porque a ordem
das chaves num `dict` é indefinida e pode mudar entre versões de Python.
    
    >>> sorted(ufs.keys()) 
    ['AM', 'RJ', 'SC']
    >>> sorted(ufs.items())
    [('AM', 'Amazonas'), ('RJ', 'Rio de Janeiro'), ('SC', 'Santa Catarina')]
    >>> sorted(ufs.values())
    ['Amazonas', 'Rio de Janeiro', 'Santa Catarina']
    >>> 'Amazonas' in ufs.values()
    True
    
1.3. Inserção e remoção de elementos

    >>> len(ufs)
    3
    >>> ufs['PE'] = 'Pernambuco'
    >>> len(ufs)
    4
    >>> ufs['SC'] = 'Santa Cruz'
    >>> len(ufs)
    4
    >>> del ufs['AM']   
    >>> len(ufs)
    3
    >>> ufs.pop('RJ')
    'Rio de Janeiro'
    >>> 'RJ' in ufs
    False

1.4. Combinação de dicionários

    >>> len(ufs)
    2
    >>> ufs2 = dict(MG='Minas Gerais', SC='Santa Catarina', TO='Tocantins')
    >>> ufs.update(ufs2)
    >>> len(ufs)
    4
    >>> ufs['SC']
    'Santa Catarina'
    >>> sorted(ufs.keys())
    ['MG', 'PE', 'SC', 'TO']
    
'''

if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags = opcoes)

