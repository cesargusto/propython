"""
    >>> from math import sin, pi
    >>> Planilha.tools.update(sin=sin, pi=pi, len=len)
    >>> p = Planilha()
    >>> p['a1'] = '5'
    >>> p['a2'] = 'a1*6'
    >>> p['a3'] = 'a2*7'
    >>> p['a3']
    210
    >>> p['b1'] = 'sin(pi/4)'
    >>> p['b1']
    0.70710678118654746
    >>> p.getformula('b1')
    'sin(pi/4)'
"""

class Planilha:
    _cells = {}
    tools = {}
    def __setitem__(self, key, formula):
        self._cells[key] = formula
    def getformula(self, key):
        return self._cells[key]
    def __getitem__(self, key ):
        return eval(self._cells[key], Planilha.tools, self)

if __name__=='__main__':
    import doctest
    doctest.testmod()
