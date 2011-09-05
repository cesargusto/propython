#!/usr/bin/env python

'''

    >>> b = Box(3)
    >>> b.probe(2, 2)
    Traceback (most recent call last):
    ValueError: (2, 2) is not an edge cell
    >>> b.probe(-1, 2)
    Vector(3, 2)
    >>> b.probe(1, -1)
    Vector(1, 3)

'''

from pprint import pprint

EMPTY = 0
ATOM = 1

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)
    def __repr__(self):
        return 'Vector{0}'.format((self.x, self.y))
    def edge(self, box):
        return box.edge(self.x) != box.edge(self.y)

class Box(object):
    def __init__(self, width):
        self.width = width
        self.array = dict(((x,y),EMPTY) for x in range(width)
                                        for y in range(width))
    def __getitem__(self, xy):
        return self.array[xy]

    def edge(self, n):
        return n == -1 or n == self.width

    def probe(self, x, y):
        cell = Vector(x, y)
        if not cell.edge(self):
            raise ValueError('{0} is not an edge cell'.format((x,y)))
        if self.edge(x):
            direction = Vector(1,0) if x == -1 else Vector(-1,0)
        else:
            direction = Vector(0,1) if y == -1 else Vector(0,-1)
        while True:
            cell += direction
            if cell.edge(self): break
        return cell

if __name__=='__main__':
    import doctest
    doctest.testmod()
