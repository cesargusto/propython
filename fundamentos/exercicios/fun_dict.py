#!/usr/bin/env python
# coding: utf-8

# INSTRUÇÕES:
# - implemente funções que satisfaçam os testes apresentados  
#
# - a opção REPORT_ONLY_FIRST_FAILURE faz aparecer apenas o primeiro 
#   teste quebrado no relatório de testes
#
# - se quiser deixar um exercício para depois, coloque o comentário 
#   "# doctest: +SKIP" na linha de entrada, por exemplo:
#
#   >>> 2 ** 100 # doctest: +SKIP
#   XXX

'''
Exercícios de funções para manipular dicionários e tuplas
'''

def parar(nave):
    ''' zera a velocidade da nave nos três eixos
    
        >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5))
        >>> parar(nave)
        >>> nave['vel']
        (0, 0, 0)
    '''

def mover(nave):
    ''' atualiza a posicao, de acordo com a velocidade atual
    
        >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5))
        >>> mover(nave)
        >>> nave['pos']
        (10, 0, 4)
        >>> mover(nave)
        >>> nave['pos']
        (10, -5, -1)
    '''

def acelerar(nave, ax=None, ay=None, az=None):
    ''' altera zero ou mais acelerações e atualiza a velocidade da nave
    
        >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5), acel=(0,2,-1))
        >>> acelerar(nave, ay=4)
        >>> nave['acel']
        (0, 4, -1)
        >>> nave['vel']
        (0, -1, -6)
        >>> acelerar(nave)
        >>> nave['acel']
        (0, 4, -1)
        >>> nave['vel']
        (0, 3, -7)
    '''

if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags = opcoes)
    
