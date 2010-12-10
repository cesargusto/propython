#!/usr/bin/env python

'''
    >>> l = Livro('123')
    Traceback (most recent call last):
      ...
    ValueError: ISBN deve ter 13 caracteres
    >>> l = Livro('1234567890123')
    >>> l.isbn
    '1234567890123'
    >>> l.isbn = '666'
    Traceback (most recent call last):
      ...
    ValueError: ISBN deve ter 13 caracteres
'''

class CampoChar(object):
    def __init__(self, nome, max_len):
        self.nome = nome
        self.max_len = max_len
        self.nome_atr = '__'+self.nome.lower()
    def __get__(self, instance, cls):
        return getattr(instance, self.nome_atr)
    def __set__(self, instance, valor):
        if len(valor) != self.max_len:
            raise ValueError('%s deve ter %s caracteres' %
                (self.nome, self.max_len))
        setattr(instance, self.nome_atr, valor)

class Livro(object):

    def __init__(self, isbn):
        self.isbn = isbn

    isbn = CampoChar('ISBN', max_len=13)

if __name__=='__main__':
    import doctest
    doctest.testmod()
