#!/usr/bin/env python
# coding: utf-8

"""
Em Python os atributos de uma classe são armazenados em um `dict`, portanto
sua ordem não é preservada. Normalmente a ordem não realmente importante.

Note no exemplo abaixo que a lista devolvida por `dir(l)` não preserva
a ordem em que foram declarados os atributos na classe `Livro`::

    >>> class LivroSimples(object):
    ...     titulo = u''
    ...     isbn = u''
    ...     autores = u''
    >>> l = LivroSimples()
    >>> dir(l) #doctest: +ELLIPSIS
    [...'autores', 'isbn', 'titulo'...]
    
Para gerar formulários automaticamente a partir da classe, é desejável
respeitar a ordem de declaração dos campos. Usando descritores e uma 
metaclasse, é possível preservar esta ordem.

    >>> class Livro(OrderedModel):
    ...     titulo = OrderedProperty(required=True)
    ...     isbn = OrderedProperty()
    ...     autores = PluralProperty(required=True)
    >>> l2 = Livro()
    >>> l2.titulo = 'O Alienista'
    >>> l2.titulo
    'O Alienista'
    >>> list(l2)
    ['titulo', 'isbn', 'autores']
    >>> for campo in l2: print campo
    titulo
    isbn
    autores
    >>> l3 = Livro()
    >>> l3.titulo is None
    True
    >>> l4 = Livro(titulo=u'Alice', autores=[u'Carroll', u'Tenniel'], isbn=u'9781234567890')
    >>> for campo, valor in l4.iteritems():
    ...     print '%-8s: %s' % (campo, valor)
    titulo  : Alice
    isbn    : 9781234567890
    autores : [u'Carroll', u'Tenniel']
    
Os descritores têm um atributo `order` que é inicializado com um contador da 
classe `OrderedProperty` incrementado a cada nova instância. A metaclasse usa
este atributo `order` para ordenar uma lista com os nomes dos campos.

O método booleano `isplural` informa se o atributo nomeado é plural::

    >>> for campo in l4:
    ...     print '%-8s: %s' % (campo, l4.isplural(campo))
    titulo  : False
    isbn    : False
    autores : True

O método `iteritemsplural` devolve um iterador de triplas com o nome do campo,
o valor, e um booleano indicando se é plural, facilitando a formatação dos valores::

    >>> for campo, valor, plural in l4.iteritemsplural():
    ...     valor = '; '.join(valor) if plural else valor
    ...     print '%-8s: %s' % (campo, valor)
    titulo  : Alice
    isbn    : 9781234567890
    autores : Carroll; Tenniel

Aos descritores `PluralProperty` só é permitido atribuir tuplas, listas ou 
instâncias de subclasses destes tipos::

    >>> l5 = Livro(autores=u'Fulano')
    Traceback (most recent call last):
      ...
    TypeError: PluralProperty must satisfy isinstance(value, (tuple, list))
    >>> l5 = Livro(autores=[])

Para validar propriedades obrigatórias, há o método check::

    >>> l4.check() # livro completo, nenhuma mensagem de erro
    {}
    >>> l6 = Livro()
    >>> l6.check()
    {'titulo': u'Required value missing.', 'autores': u'Required value missing.'}
    >>> l7 = Livro(titulo=u'Jangada de Pedra')
    >>> l7.check()
    {'autores': u'Required value missing.'}
    
No caso de propriedades plurais como `autores`, `check` verifica se há pelo
menos um item na propriedade, e se este item tem conteúdo::
    
    >>> l8 = Livro(titulo=u'Jangada de Pedra', autores=[])
    >>> l8.check()
    {'autores': u'Required value missing.'}
    >>> l9 = Livro(titulo=u'Jangada de Pedra', autores=[u''])
    >>> l9.check()
    {'autores': u'Required value missing.'}
    >>> l10 = Livro(titulo=u'Jangada de Pedra', autores=[u'Saramago'])
    >>> l10.check()
    {}

Na definição de uma propriedade, pode-se passar uma função de validação que
aceita um valor e realiza um testeo, devolvendo uma string vazia se o valor
passar no teste, ou uma mensagem de erro se o valor não passar::

    >>> class Produto(OrderedModel):
    ...     nome = OrderedProperty(required=True)
    ...     estoque = NumberProperty(required=True)
    ...     preco = NumberProperty(required=True, validator=lambda p:u'Deve ser maior que zero' if p<=0 else '')
    >>> p1 = Produto(nome='rebimboca', estoque=0, preco=0)
    >>> p1.check()
    {'preco': u'Deve ser maior que zero'}
    >>> p2 = Produto(nome='rebimboca', estoque=0, preco=9.99)
    >>> p2.check()
    {}
   
"""

from operator import attrgetter
        
class OrderedProperty(object):
    __count = 0
    
    def __init__(self, required=False, validator=None):
        self.order = self.__class__.__count
        self.__class__.__count += 1
        self.required = required
        self.validator = validator
        
    def __get__(self, instance, cls):
        return getattr(instance, self.name, None)
        
    def __set__(self, instance, value):
        setattr(instance, self.name, value)
        
    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)
        
    def check(self, instance):
        value = getattr(instance, self.name, None)
        if self.required:
            if not value:
                return u'Required value missing.'
        if self.validator: # and value is not None:
            return self.validator(value)

class PluralProperty(OrderedProperty):

    def __set__(self, instance, value):
        if isinstance(value, (tuple, list)):
            setattr(instance, self.name, value)
        else:
            raise TypeError('PluralProperty must satisfy isinstance(value, (tuple, list))')

    def check(self, instance):
        if self.required:
            value = getattr(instance, self.name, None)
            if value is None or len(value) == 0 or not value[0]:
                return u'Required value missing.'

class NumberProperty(OrderedProperty):

    def __set__(self, instance, value):
        if isinstance(value, (int, long, float)):
            setattr(instance, self.name, value)
        else:
            raise TypeError('NumberProperty must be int, long or float')

    def check(self, instance):
        value = getattr(instance, self.name, None)
        if self.required:
            if value is None:
                return u'Required value missing.'
        if self.validator: # and value is not None:
            return self.validator(value)

class OrderedMeta(type):
    def __new__(cls, name, bases, dict):
        props = []
        for key, attr in dict.items():
            if isinstance(attr, OrderedProperty):
                attr.name = '_' + key
                props.append(attr)
        cls._ordered_props = sorted(props, key=attrgetter('order'))
        return type.__new__(cls, name, bases, dict)

class OrderedModel(object):
    __metaclass__ = OrderedMeta

    def __init__(self, **kwargs):
        for k in kwargs:
            setattr(self, k, kwargs[k])
    
    def __iter__(self):
        return (prop.name[1:] for prop in self.__class__._ordered_props)

    def iteritems(self):
        return ((prop.name[1:], getattr(self, prop.name)) 
                for prop in self.__class__._ordered_props)
                
    def isplural(self, name):
        return isinstance(self.__class__.__getattribute__(self.__class__, name), PluralProperty)

    def iteritemsplural(self):
        return ((prop.name[1:], getattr(self, prop.name), self.isplural(prop.name[1:]))
                for prop in self.__class__._ordered_props)

    def check(self):
        msgs = {}
        for prop in self:
            msg = self.__class__.__getattribute__(self.__class__, prop).check(self)
            if msg:
                msgs[prop] = msg
        return msgs            


if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    
