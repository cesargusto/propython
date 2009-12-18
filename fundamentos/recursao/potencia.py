#!/usr/bin/env python

'''
    >>> pot(10, 2) == 10**2
    True
    >>> pot(2, 100) == 2**100
    True
    >>> pot(1729, 7) == 1729**7
    True
    >>> from math import pi
    >>> round(pot(pi, 3),6) == round(pi**3, 6)
    True

'''

def pot(x, y):
    if y == 0:
        return 1
    p = pot(x, y/2)
    if y % 2:
        return p * p * x
    else:
        return p * p

if __name__=='__main__':
    import doctest
    doctest.testmod()
