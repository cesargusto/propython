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
    p = nave['pos']
    v = nave['vel']
    nave['pos']=((p[0]+v[0]), p[1]+v[1], p[2]+v[2])
    


if __name__=='__main__':
    import doctest
    opcoes = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(optionflags = opcoes)
    
