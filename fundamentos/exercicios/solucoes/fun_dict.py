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
Exercícios de funções para manipular dicionários e tuplas
'''

def parar(veiculo):
    ''' zera a velocidade do veiculo nos três eixos
    
        >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5))
        >>> parar(nave)
        >>> nave['vel']
        (0, 0, 0)
    '''
    veiculo['vel'] = (0, 0, 0)

def mover(veiculo):
    ''' atualiza a posicao, de acordo com a velocidade atual
    
        >>> nave = dict(pos=(10,5,9), vel=(0,-5,-5))
        >>> mover(nave)
        >>> nave['pos']
        (10, 0, 4)
        >>> mover(nave)
        >>> nave['pos']
        (10, -5, -1)
    '''
    x, y, z = veiculo['pos']
    vx, vy, vz = veiculo['vel']
    veiculo['pos'] = (x+vx, y+vy, z+vz)

def acelerar(veiculo, ax=None, ay=None, az=None):
    ''' altera zero ou mais acelerações e atualiza a velocidade do veiculo
    
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
    ax0, ay0, az0 = veiculo['acel']
    if ax is None: ax = ax0
    if ay is None: ay = ay0
    if az is None: az = az0
    veiculo['acel'] = (ax, ay, az)
    vx, vy, vz = veiculo['vel']
    veiculo['vel'] = (vx+ax, vy+ay, vz+az)
    

if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags = opcoes)
    
