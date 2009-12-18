#!/usr/bin/env python

'''
    >>> pot(10, 0)
    1
    >>> pot(10, 5)
    100000
    >>> pot(2, 100) == 2**100
    True
    >>> pot(1729, 1)
    1729
    >>> pot(1729, 7) == 1729**7
    True
    >>> from math import pi
    >>> round(pot(pi, 3), 6) == round(pi**3, 6)
    True
    >>> pot(2, 1729) == 2**1729
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
