
from pprint import pprint

EMPTY = 0
ATOM = 1

class Box(object):
    def __init__(self, width):
        self.width = width
        self.array = dict(((x,y),EMPTY) for i in range(width) 
                                        for j in range(width))
    def __getitem__(self, xy):
        return self.array[xy]

    def border(self, n):
        return n == 0 or n == (width-1)

    def probe(self, x, y):
        pass
