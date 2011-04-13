"""
>>> from math import sin, pi
>>> p = Planilha(seno=sin, pi=pi)
>>> p['a1'] = '2'
>>> p['a2'] = 'a1*3'
>>> p['a3'] = 'a2*7'
>>> p['a3']
42
>>> p['a1'] = '5'
>>> p['a3']
105
>>> p['b1'] = 'seno(pi/4)'
>>> p['b1']
0.70710678118654746
>>> p.formula('b1')
'seno(pi/4)'
"""

class Planilha(object):
    _cels = {}
    _funcs = {}
    def __init__(self, **funcs):
        self._funcs.update(funcs)
    def formula(self, chave):
        return self._cels[chave]
    def __setitem__(self, chave, formula):
        self._cels[chave] = formula
    def __getitem__(self, chave):
        return eval(self._cels[chave], self._funcs, self)

if __name__ == "__main__":
    import doctest
    print doctest.testmod()

