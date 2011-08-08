# coding: utf-8
# Módulo testado em Python 2 e Python 3

'''
Um ``Treco`` pode ser inicializado com quaisquer argumentos, e os argumentos
se tornam seus atributos::

    >>> t = Treco(a=1, b=2)
    >>> t
    Treco(a=1, b=2)

Note que a representação do ``Treco`` é uma string com o código que
inicializaria uma instância igual de ``Treco``.

O dunder-setater (é assim que se fala __setattr__) é programado para
(1) criar ou sobrecrever o atributo no __dict__ da instância, e 
(2) fazer um ``print`` para mostrar o que foi feito::

    >>> x = Treco()
    >>> x.a = 10
    self.__setattr__('a', 10)
    >>> x.a
    10
    >>> x.b = 20
    self.__setattr__('b', 20)
    >>> x
    Treco(a=10, b=20)

Agora o teste da atribuição em cascata::

    >>> x.a = x.b = x.c = 3
    self.__setattr__('a', 3)
    self.__setattr__('b', 3)
    self.__setattr__('c', 3)

Note que as atribuições acontecem da esquerda para a direita, muito embora
a gente saiba que o valor a ser atribuído (3 neste caso) é avaliado primeiro.

Eis uma pequena prova disso::

    >>> def nove():
    ...     print('nove!')
    ...     return 9
    >>> x.a = x.b = x.c = nove()
    nove!
    self.__setattr__('a', 9)
    self.__setattr__('b', 9)
    self.__setattr__('c', 9)

'''


class Treco(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        print('self.__setattr__(%r, %r)' % (attr, value))

    def __repr__(self):
        return 'Treco(%s)' % ', '.join('%s=%s'%(k,v) for k,v in self.__dict__.items())

if __name__=='__main__':
    import doctest
    doctest.testmod()
