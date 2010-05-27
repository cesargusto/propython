#!/usr/bin/env python

"""
    >>> l = Livro()
    >>> l.atributos()
    ['autores', 'isbn', 'titulo']

"""
    
class Livro(object):
    titulo = u''
    isbn = u''
    autores = u''
    
    def atributos(self):
        ''' devolve lista de atributos que nao sao metodos '''
        return [atr for atr in dir(obj) if not atr.startswith('__')
            and not hasattr(getattr(obj, atr),'__call__')]
    
class OrderedProperty(object):
    _count = 0
    def __init__(self):
        self.order = self.__class__._count
        self.__class__._count += 1
        
class OrderedMeta(type):
    def __new__(cls, name, bases, dict):
        _ordered_props = []
        for key, value in dict.items():
            if isinstance(value, OrderedProperty)        
    
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
