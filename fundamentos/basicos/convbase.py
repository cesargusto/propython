#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
========================================================================
Funções para conversão de entre bases numéricas com dígitos arbitrários
========================================================================

Estas funções permitem especificar qualquer sequência de caracteres como
"dígitos". Uma aplicação útil é gerar identificadores alfanuméricos que 
usam todos os dígitos e letras ASCII, exceto "1", "l", "0" e "O", evitando
confusões na transcrição (veja os exemplos que usam os dígitos BASE32).

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
    
Para gerar identificadores curtos, use base 36 ou base 32::

    >>> calcbase('xyz', BASE36)
    44027
    >>> calcbase('abcd', BASE36)
    481261
    >>> calcbase('kf12oi', BASE36)
    1234567890
    >>> calcbase('setecastronomy1992', BASE36)
    8140250869386925000618385174L

Para evitar confusão, esta definição de base 32 não usa os dígitos '1', 'l',
'0' ou 'o'. Assim, o dígito que vale zero é '2', e o que vale um é '3'::

    >>> BASE32
    '23456789abcdefghijkmnpqrstuvwxyz'
    >>> calcbase('2', BASE32)
    0
    >>> calcbase('3', BASE32)
    1
    >>> calcbase('32', BASE32)
    32
    >>> calcbase('39', BASE32)
    39
    >>> calcbase('3a', BASE32)
    40
    >>> calcbase('3z', BASE32)
    63
    >>> calcbase('zz', BASE32)
    1023
    >>> calcbase('322', BASE32)
    1024
    >>> calcbase('xyz', BASE32)
    30687
    >>> calcbase('zzz', BASE32)
    32767
    >>> calcbase('abcd', BASE32)
    271691
    >>> calcbase('36te2qk', BASE32)
    1234567890
    >>> calcbase('abc123', BASE32) #doctest: +ELLIPSIS
    Traceback (most recent call last):
      ...
    ValueError: digito invalido: "1" nao ocorre em "23456789...kmnpqrstuvwxyz"
    
------------------------------------------------------------------------
`reprbase`: representação de inteiro em uma base numérica qualquer
------------------------------------------------------------------------

    >>> reprbase(10, '01')
    '1010'
    >>> reprbase(42, 'ACGT')
    'GGG'
    >>> reprbase(0, 'ACGT')
    'A'
    >>> reprbase(0, HEXA)
    '0'
    >>> reprbase(481261, BASE36)
    'abcd'
    >>> reprbase(1234567890, BASE32)
    '36te2qk'
    >>> reprbase(0, BASE32) # BASE32 não tem '0', '1', 'l' ou 'o'
    '2'
    >>> reprbase(32, BASE32)
    '32'
    >>> reprbase(64, BASE32)
    '42'
    >>> reprbase(1000, BASE32)
    'za'
    >>> reprbase(1024, BASE32)
    '322'
    >>> reprbase(2**32, BASE32)
    '6222222'
    >>> reprbase(2**64, BASE32)
    'i222222222222'
    
------------------------------------------------------------------------------
`convbase`: conversão entre bases numéricas quaisquer, com dígitos arbitrários
------------------------------------------------------------------------------

    >>> import string
    >>> convbase('GGG', 'ACGT', '01')
    '101010'
    >>> convbase('101010', '01', string.digits)
    '42'
    >>> convbase('64202', string.digits, HEXA)
    'faca'
    >>> convbase(convbase('abc123', BASE36, BASE32), BASE32, BASE36)
    'abc123'

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

HEXA = string.hexdigits[:16] # remover digitos maiusculos
BASE36 = string.digits+string.ascii_lowercase
BASE32 = ''.join(d for d in BASE36 if d not in '1l0o')

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
    return s if s else digitos[0]
    
def convbase(s, digitos_de, digitos_para):
    ''' converte entre bases numéricas quaisquer, com dígitos arbitrários '''
    return reprbase(calcbase(s, digitos_de), digitos_para)
    
if __name__=='__main__':
    import doctest
    doctest.testmod()

