#!/usr/bin/env python
# coding: utf-8

'''
    >>> for i in [letra for letra in busca_letra()]:
    ...    print i
    ... 
    buscando "A"
    buscando "B"
    buscando "C"
    A
    B
    C
    >>> for i in (letra for letra in busca_letra()):
    ...    print i
    ... 
    buscando "A"
    A
    buscando "B"
    B
    buscando "C"
    C
'''

def busca_letra(ultima='C'):
    cod = ord('A')
    while chr(cod) <= ultima:
        letra = chr(cod)
        print 'buscando "%s"' % letra
        yield letra
        cod += 1

if __name__=='__main__':
    import doctest
    doctest.testmod()
