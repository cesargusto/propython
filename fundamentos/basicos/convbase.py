#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
-----------------------------------------------------------------
`calcbase`: conversão de inteiro para uma base numérica qualquer
-----------------------------------------------------------------

A função `calcbase` aceita qualquer série de dígitos, mas vamos começar com 
casos comuns::

    >>> [calcbase(i, HEXA) for i in ('9','a','f','10','1f', 'ff', 'faca')]
    [9, 10, 15, 16, 31, 255, 64202]
    >>> [calcbase(i, '01') for i in ('0','1','10','1010','1111')]
    [0, 1, 2, 10, 15]
    >>> calcbase('1'*64, '01') == 2**64-1
    True

Especificando os dígitos A, C, G e T podemos vamos transformar sequências de 
DNA em números::

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
    
Para gerar identificadores curtos, a base 36 é uma ótima opção::

    >>> from string import digits, ascii_lowercase
    >>> base36 = digits+ascii_lowercase
    >>> calcbase('abcd', base36)
    481261
    >>> calcbase('kf12oi', base36)
    1234567890
    >>> calcbase('setecastronomy1992', base36)
    8140250869386925000618385174L
    
------------------------------------------------------------------------
`reprbase`: representação de inteiro em para uma base numérica qualquer
------------------------------------------------------------------------

    >>> reprbase(10,'01')
    '1010'
    >>> reprbase(42,'ACGT')
    'GGG'
    >>> reprbase(481261,base36)
    'abcd'
    >>> reprbase(1234567890,base36)
    'kf12oi'

------------------------------------------------------------------------------
`convbase`: conversão entre bases numéricas quaisquer, com dígitos arbitrários
------------------------------------------------------------------------------

    >>> convbase('GGG', 'ACGT', '01')
    '101010'
    >>> convbase('101010', '01', digits)
    '42'
    >>> convbase('64202', digits, HEXA)
    'faca'

--------------------
Tratamento de erros
--------------------

Como em Python praticamente não há overflow de inteiros, o erro mais provável
ao usar estas funções é não existir um dígito na base numérica especificada::

    >>> calcbase('102', '01')
    Traceback (most recent call last):
      ...
    ValueError: digito invalido: "2" nao ocorre em "01"
    
'''

import string

DECIMAL = string.digits
HEXA = string.hexdigits[:16] # remover digitos maiusculos
BASE36 = string.digits+string.ascii_lowercase
BASE2 = '01'

def calcbase(s, digitos):
    ''' devolve o valor de `s` na base numérica representada por `digitos`
    
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
    
def calcbase2(s, digitos):
    ''' a mesma função `calcbase`, implementada em estilo funcional '''
    return sum(digitos.index(dig)*len(digitos)**pot 
               for pot, dig in enumerate(reversed(s)))

def reprbase(n, digitos):
    ''' devolve a representação do valor `n` na base `len(digitos)` '''
    base = len(digitos)
    s = ''
    while n:
        n, d = divmod(n, base)
        s = digitos[d] + s
    return s if s else '0'
    
def convbase(s, digitos_de, digitos_para):
    ''' converte entre bases numéricas quaisquer, com dígitos arbitrários '''
    return reprbase(calcbase(s, digitos_de), digitos_para)
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

