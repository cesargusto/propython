# coding: utf-8

'''
Source: http://en.wikipedia.org/wiki/Fixed_point_combinator

A version of the Y combinator that can be used in call-by-value
(applicative-order) evaluation is given by η-expansion of part
of the ordinary Y combinator:

    Z = λf. (λx. f (λy. x x y)) (λx. f (λy. x x y))

Here is an example of this in Python::

    >>> fact(5)
    120
    >>> fact(20)
    2432902008176640000
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6

'''

Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x:
                                       f(lambda *args: x(x)(*args)))
@Z
def fact(f):
    return lambda x: 1 if x == 0 else x * f(x-1)


import doctest
print doctest.testmod()

