# coding: utf-8

from math import sqrt

class Vetor(object):
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        
    def __repr__(self):
        return 'Vetor(%s, %s, %s)' % (self.a, self.b, self.c)

    def distancia(self, v2):
        '''
            >>> v = Vetor(1,1,1)
            >>> p1 = Vetor(2,1,1)
            >>> p2 = Vetor(3,1,1)
            >>> p1.distancia(p2) # doctest: +ELLIPSIS
            1.0...
            
        '''
        da = self.a - v2.a
        db = self.b - v2.b
        dc = self.c - v2.c
        return sqrt( da**2 + db**2 + dc**2  )

    def distancia_abs(self):
        return self.distancia(Vetor(0,0,0))
            
    def somar(self, v2):
        '''
            >>> pos = Vetor(1,1,1)
            >>> vel = Vetor(1,2,3)
            >>> pos2 = pos.somar(vel)
            >>> pos2
            Vetor(2, 3, 4)
        
        '''
        da = self.a + v2.a
        db = self.b + v2.b
        dc = self.c + v2.c
        return Vetor(da,db,dc)
        
    def __add__(self, other):
        '''
            >>> pos = Vetor(1,1,1)
            >>> vel = Vetor(1,2,3)
            >>> pos + vel
            Vetor(2, 3, 4)
        '''
        
        return self.somar(other)

if __name__=='__main__':
    import doctest
    doctest.testmod()
    
    