import roman
import sys

_este_modulo = sys.modules[__name__]

class Romano(int):

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return roman.toRoman(self.valor)

    __repr__ = __str__

    def __int__(self):
        return self.valor

    def __add__(self, outro):
        return Romano(self.valor+int(outro))

    __radd__ = __add__

__all__ = ['Romano']

for i in range(1, 4000):
    r = Romano(i)
    r_str = str(r)
    _este_modulo.__dict__[r_str] = r
    __all__.append(r_str)

