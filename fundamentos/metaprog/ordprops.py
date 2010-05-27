#!/usr/bin/env python

"""
    >>> l = Livro()
    >>> l.atributos()
    ['autores', 'isbn', 'titulo']
    >>> l2 = Livro2()
    >>> l2.titulo = 'O Alienista'
    >>> l2.titulo
    'O Alienista'
    >>> l2.atributos()
    ['autores', 'isbn', 'titulo']
    >>> l2.atributos_ordenados()
    ['titulo', 'isbn', 'autores']

"""

from operator import attrgetter
    
def nao_metodos(obj):
    ''' devolve lista de atributos que nao sao metodos '''
    return [atr for atr in dir(obj) if not atr.startswith('__')
        and not hasattr(getattr(obj, atr),'__call__')]

class Livro(object):
    titulo = u''
    isbn = u''
    autores = u''
    
    def atributos(self):
        return nao_metodos(self)
    
class OrderedProperty(object):
    _count = 0
    def __init__(self):
        self.order = self.__class__._count
        self.__class__._count += 1
        self.value = None
    def __get__(self, instance, cls):
        return self.value
    def __set__(self, instance, value):
        self.value = value
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)

class OrderedMeta(type):
    def __new__(cls, name, bases, dict):
        cls._ordered_props = []
        for key, value in dict.items():
            if isinstance(value, OrderedProperty):
                value.name = '_' + key
                cls._ordered_props.append(value)
        cls._ordered_props.sort(key=attrgetter('order'))
        return type.__new__(cls, name, bases, dict)

class OrderedModel(object):
    __metaclass__ = OrderedMeta

    def ordered_props(self):
        return [prop.name[1:] for prop in self.__class__._ordered_props]
    
class Livro2(OrderedModel):
    titulo = OrderedProperty()
    isbn = OrderedProperty()
    autores = OrderedProperty()

    def __init__(self, titulo=None):
        self.titulo = titulo

    def atributos(self):
        return nao_metodos(self)

    def atributos_ordenados(self):
        ''' devolve lista de atributos ordenados '''
        return self.ordered_props()
    
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
