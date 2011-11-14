# coding: utf-8

"""
    >>> l = Livro(99)
    >>> l.paginas
    99
    >>> print Livro.paginas.__doc__ #doctest: -SKIP
    Número de páginas
    >>> l.paginas = 10
    >>> l.paginas
    10
    >>> l.paginas = 0
    Traceback (most recent call last):
      ...
    ValueError: n deve ser maior que zero
"""

class Livro(object):
    def __init__(self, paginas):
        self.paginas=paginas
    def getPaginas(self): 
        return self.__paginas
    def setPaginas(self, num): 
        if num <= 0:
            raise ValueError, 'n deve ser maior que zero'
        self.__paginas = num
    def delPaginas(self): 
        del self.__paginas
    paginas = property(getPaginas, setPaginas, delPaginas, 'Número de páginas')

if __name__=='__main__':
    import doctest
    doctest.testmod()    
