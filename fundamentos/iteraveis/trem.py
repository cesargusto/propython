#/usr/bin/env python3

'''
    >>> t = Trem(4)
    >>> len(t)
    4
    >>> t[0]
    'vagao #1'
    >>> t[3]
    'vagao #4'
    >>> t[-1]
    'vagao #4'
    >>> t[4]
    Traceback (most recent call last):
      ...
    IndexError: vagao inexistente 4 (primeiro=0)

'''

class Trem(object):
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes
    def __len__(self):
        return self.num_vagoes
    def __getitem__(self, pos):
        indice = pos if pos >= 0 else self.num_vagoes + pos
        if 0 <= indice < self.num_vagoes: # indice 2 -> vagao #3
            return 'vagao #%s' % (indice+1)
        else:
            raise IndexError('vagao inexistente %s (primeiro=0)' % pos)

