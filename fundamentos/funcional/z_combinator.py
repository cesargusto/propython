# coding: utf-8

'''
Source: http://en.wikipedia.org/wiki/Fixed_point_combinator

A version of the Y combinator that can be used in call-by-value 
(applicative-order) evaluation is given by η-expansion of part 
of the ordinary Y combinator:

    Z = λf. (λx. f (λy. x x y)) (λx. f (λy. x x y))

Here is an example of this in Python::

    >>> Z = lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: 
    ...                                        f(lambda *args: x(x)(*args)))
    >>> fact = lambda f: lambda x: 1 if x == 0 else x * f(x-1)
    >>> Z(fact)(5)
    120
    >>> Z(fact)(20)
    2432902008176640000
    >>> Z(fact)(0)
    1
    >>> Z(fact)(1)
    1
    >>> Z(fact)(2)
    2
    >>> Z(fact)(3)
    6
    
'''

import doctest
print doctest.testmod()
    
