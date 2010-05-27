#!/usr/bin/env python

"""
    >>> l = Livro()
    >>> l.atributos()
    ['autores', 'isbn', 'titulo']

"""

def non_methods(obj):
    return [atr for atr in dir(obj) if not atr.startswith('__')
        and not hasattr(getattr(obj, atr),'__call__')]
    
class Livro(object):
    titulo = u''
    isbn = u''
    autores = u''
    
    def atributos(self):
        return non_methods(self)
    
class OrderedProperty(object):
    def __init__(self):
        pass    
    
    
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
