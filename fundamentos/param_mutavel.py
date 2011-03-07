#!/usr/bin/env python

"""
    >>> def incr(x):
    ...   x += 1
    >>> n = InteiroMutavel(11)
    >>> print n + 1
    12
    >>> print n
    11
    >>> n += 1
    >>> n
    12
    >>> incr(n)
    >>> n
    13

"""

class InteiroMutavel(object):
    def __init__(self, valor):
        self.valor = valor
        
    def __repr__(self):
        return str(self.valor)    
        
    def __add__(self, i):
        return InteiroMutavel(self.valor + i)
        
    def __iadd__(self, i):
        self.valor += i
        return self

if __name__=='__main__':
    import doctest
    doctest.testmod()

