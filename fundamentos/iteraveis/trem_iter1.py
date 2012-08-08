#/usr/bin/env python3

'''
    >>> t = Trem(4)
    >>> for vagao in t:
    ...   print(vagao)
    vagao #1
    vagao #2
    vagao #3
    vagao #4

'''

class Trem(object):
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes
    def __iter__(self):
        return IteradorTrem(self.num_vagoes)

class IteradorTrem(object):
    def __init__(self, num_vagoes):
        self.atual = 0
        self.ultimo_vagao = num_vagoes - 1  
    def next(self):
        if self.atual <= self.ultimo_vagao:
            self.atual += 1
            return 'vagao #%s' % (self.atual) # indice 2 -> vagao #3
        else:
            raise StopIteration()

