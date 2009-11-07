#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    >>> Coisa.faz()
    Faz algo com a classe <Coisa>
    >>> Coisa.bla()
    Eu poderia ser uma função global

'''
class Coisa(object):
    def faz(cls):
        print 'Faz algo com a classe <%s>' % cls.__name__
    faz = classmethod(faz)

    def bla():
        print 'Eu poderia ser uma função global'
    bla = staticmethod(bla)

class Coisa(object):
    @classmethod
    def faz(cls):
        print 'Faz algo com a classe <%s>' % cls.__name__

    @staticmethod
    def bla():
        print 'Eu poderia ser uma função global'

if __name__=='__main__':
    import doctest
    doctest.testmod()

