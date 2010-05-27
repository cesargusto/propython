#!/usr/bin/env python
# coding: utf-8

"""
Em Python os atributos de uma classe são armazenados em um dict, portanto
sua ordem não é preservada (normalmente a ordem não é mesmo importante).

    >>> def nao_metodos(obj):
    ...     ''' devolve lista de atributos que nao sao metodos '''
    ...     return [atr for atr in dir(obj) if not atr.startswith('__')
    ...             and not hasattr(getattr(obj, atr),'__call__')]
    >>> class Livro(object):
    ...     titulo = u''
    ...     isbn = u''
    ...     autores = u''
    >>> l = Livro()
    >>> nao_metodos(l)
    ['autores', 'isbn', 'titulo']
    
Note no exemplo acima que a lista devolvida por nao_metodos não preserva
a ordem em que foram declarados os atributos na classe Livro.

Usando um descritores e uma metaclasse, é possível preservar a ordem dos
atributos::

    >>> class Livro2(OrderedModel):
    ...     titulo = OrderedProperty()
    ...     isbn = OrderedProperty()
    ...     autores = OrderedProperty()
    >>> l2 = Livro2()
    >>> l2.titulo = 'O Alienista'
    >>> l2.titulo
    'O Alienista'
    >>> nao_metodos(l2)
    ['autores', 'isbn', 'titulo']
    >>> l2.ordered_props()
    ['titulo', 'isbn', 'autores']

"""

from operator import attrgetter
        
class OrderedProperty(object):
    _count = 0
    def __init__(self):
        self.order = self.__class__._count
        self.__class__._count += 1
    def __get__(self, instance, cls):
        return getattr(self, 'value', None)
    def __set__(self, instance, value):
        self.value = value
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)

class OrderedMeta(type):
    def __new__(cls, name, bases, dict):
        props = []
        for key, value in dict.items():
            if isinstance(value, OrderedProperty):
                value.name = '_' + key
                props.append(value)
        cls._ordered_props = sorted(props, key=attrgetter('order'))
        return type.__new__(cls, name, bases, dict)

class OrderedModel(object):
    __metaclass__ = OrderedMeta

    def ordered_props(self):
        return [prop.name[1:] for prop in self.__class__._ordered_props]
        
if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
