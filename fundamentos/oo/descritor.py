# coding: utf-8

"""
    >>> l = Livro(99)
    >>> l.paginas
    99
    >>> print Livro.paginas.__doc__ #doctest: +SKIP
    Número de páginas
    >>> l.paginas = 10
    >>> l.paginas
    10
    >>> l.paginas = 0
    Traceback (most recent call last):
      ...
    ValueError: n deve ser maior que zero
"""

class NumeroNatural(object):
    def __init__(self, name=None, doc=''):
        if name is None:
            self.name = self.__class__.__name__+repr(id(self))
        else:
            self.name = name
        self.__doc__ = doc

    def __get__(self, instance, cls):
        return getattr(instance, 'prop_'+self.name, None)
        
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError, 'n deve ser maior que zero'            
        setattr(instance, 'prop_'+self.name, value)


class Livro(object):
    paginas = NumeroNatural(doc='número de páginas')
    def __init__(self, paginas):
        self.paginas=paginas

if __name__=='__main__':
    import doctest
    doctest.testmod()    
