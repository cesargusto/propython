
'''

Watt, David - Programming Language Design Concepts
Section 16.3 Case study: Python (p. 425)

"""The compiler will not reject code that might fail with a type error,
nor even code that will certainly fail, such as:

def fail(x):
  print x+1, x[0]
"""

That is wrong, as demonstrated by this test:

    >>> ident = IdentNum(3, 'id')
    >>> print ident
    id0003
    >>> ident[0]
    'i'
    >>> ident[-1]
    '3'
    >>> print ident + 1
    id0004
    >>> def fail(x):
    ...     print x+1, x[0]
    >>> fail(ident)
    id0004 i


'''


class IdentNum(object):
    def __init__(self, num=0, prefix='', tam=4):
        self.num = num
        self.prefix = prefix
        self.tam = tam
    def __str__(self):
        return '{0}{1:0{2}d}'.format(self.prefix, self.num, self.tam)
    def __getitem__(self, i):
        return str(self)[i]
    def __add__(self, n):
        return IdentNum(self.num+n, self.prefix, self.tam)

if __name__=='__main__':
    import doctest
    doctest.testmod()
