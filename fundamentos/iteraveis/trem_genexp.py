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
        return ('vagao #%s' % (i+1) 
                    for i in range(self.num_vagoes))
