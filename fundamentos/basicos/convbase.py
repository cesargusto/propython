#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
---------------------
Testes de `calcbase`
---------------------

A função `calcbase` aceita qualquer série de dígitos, mas vamos começar com 
casos comuns::

    >>> [calcbase(i, HEXA) for i in ('9','a','f','10','1f', 'ff')]
    [9, 10, 15, 16, 31, 255]
    >>> [calcbase(i, '01') for i in ('0','1','10','1010','1111')]
    [0, 1, 2, 10, 15]
    >>> calcbase('1'*64, '01') == 2**64-1
    True

Podemos vamos transformar sequências de DNA em números::

    >>> bases_dna = 'ACGT' 
    >>> [calcbase(d, bases_dna) for d in bases_dna]
    [0, 1, 2, 3]
    >>> calcbase('GC', bases_dna) == 2 * 4 + 1 == 9
    True
    >>> calcbase('TAG', bases_dna) == 3 * 16 + 0 * 4 + 2 == 50
    True
    >>> calcbase('GGG', bases_dna)
    42
    >>> calcbase('GATTACA', bases_dna)
    9156
'''

import string

DECIMAL = string.digits
HEXA = string.hexdigits[:16] # remover digitos maiusculos
BASE36 = string.digits+string.ascii_lowercase
BASE2 = '01'

def calcbase(s, digitos=HEXA):
    ''' devolve o valor de s na base numerica representada pelos digitos
    
    A função padrão `int` faz essa conversão, mas `calcbase` aceita uma `str`
    arbitrária de dígitos que não precisa ser uma faixa contínua nem ordenada
    '''
    base = len(digitos)
    n = 0
    for pot, dig in enumerate(reversed(s)):
        try:
            val_dig = digitos.index(dig)
        except ValueError:
            msg = 'digito invalido: "%s" nao ocorre em "%s"'
            raise ValueError(msg % (dig, digitos))
        n += val_dig * (base**pot)
    return n
    
def calcbase2(s, digitos=HEXA):
    ''' a mesma função, implementada num estilo mais funcional '''
    return sum(digitos.index(dig)*len(digitos)**pot 
               for pot, dig in enumerate(reversed(s)))

def convbase(s, de=DECIMAL, para=HEXA):
    ''' a fazer... '''
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

