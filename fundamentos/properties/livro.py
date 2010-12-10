#!/usr/bin/env python

'''
    >>> l = Livro('123')
    Traceback (most recent call last):
      ...
    ValueError: ISBN deve ter 13 digitos
    >>> l = Livro('1234567890123')
    >>> l.isbn
    '1234567890123'
    >>> l.isbn = '666'
    Traceback (most recent call last):
      ...
    ValueError: ISBN deve ter 13 digitos
'''

class Livro(object):

    def __init__(self, isbn):
        self.isbn = isbn

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, valor):
        if len(valor) != 13:
            raise ValueError('ISBN deve ter 13 digitos')
        self.__isbn = valor

if __name__=='__main__':
    import doctest
    doctest.testmod()
