# coding: utf-8

"""

This module provides a xrange clone which produces series of Roman, numerals
following the collections.Sequence protocol.

The Romans had no zero, so we return an empty string for zero.::

    >>> r = RomanRange(3)
    >>> list(r)
    ['', 'I', 'II']
    >>> len(r)
    3

To skip the empty string, provide a start argument >= 1. Then the indexes
will not be in sync with the Roman numerals, but you can iterate through the
numerals easily. For example::

    >>> r1 = RomanRange(1, 4)
    >>> len(r1)
    3
    >>> r1[0], r1[1]
    ('I', 'II')
    >>> for numeral in RomanRange(1, 4):
    ...     print numeral
    I
    II
    III

Negative indexes may also be used, down to -len(r)::

    >>> r1 = RomanRange(1, 4)
    >>> r1[-1], r1[-2], r1[-3]
    ('III', 'II', 'I')
    >>> r1[-4]
    Traceback (most recent call last):
      ...
    IndexError: index out of range

The third optional argument to the constructor is a step::

    >>> r2 = RomanRange(1, 6, 2)
    >>> list(r2)
    ['I', 'III', 'V']
    >>> r2[-1], r2[-2], r2[-3]
    ('V', 'III', 'I')
    >>> list(RomanRange(1, 6, 3))
    ['I', 'IV']

Negative steps generate decrementing sequences::

    >>> r3 = RomanRange(3, 0, -1)
    >>> list(r3)
    ['III', 'II', 'I']
    >>> r3[0], r3[-1]
    ('III', 'I')
    >>> list(RomanRange(5, 0, -3))
    ['V', 'II']

Because ``RomanRange`` is a subclass of ``Sequence`` we must implement the
``__getitem__`` and ``__len__`` methods, but in return we inherit five mixin
methods::

    >>> r4 = RomanRange(1, 7)
    >>> 'III' in r4, 'X' in r4          # mixin 1: __contains__
    (True, False)
    >>> ' '.join(r4)                    # mixin 2: __iter__
    'I II III IV V VI'
    >>> ' '.join(reversed(r4))          # mixin 3: __reversed__
    'VI V IV III II I'
    >>> r4.index('III')                 # mixin 4: index
    2
    >>> r4.count('I'), r4.count('L')    # mixin 5: count
    (1, 0)

Roman numerals from I to M can only represent up to 4999:

    >>> r5 = RomanRange(5000)
    >>> r5[-1]   # 4999
    'MMMMCMXCIX'
"""

import collections

romanNumeralMap = (
    ('M',  1000), ('CM', 900), ('D',  500), ('CD', 400), ('C',  100), ('XC', 90),
    ('L',  50), ('XL', 40), ('X',  10), ('IX', 9), ('V',  5), ('IV', 4), ('I',  1))

def toRoman(n):
    """convert integer to Roman numeral, by Mark Pilgrim"""
    result = ''
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

class RomanRange(collections.Sequence):
    """A xrange clone which produces sequences of Roman numerals"""
    def __init__(self, a, b=None, step=1):
        if b is None:
            self.start, self.stop = 0, a
        else:
            self.start, self.stop = a, b
        self.step = step
        self.__check_args(self.start, self.stop, self.step)

    def __check_args(self, start, stop, step):
        if any(not isinstance(n, int) for n in (start, stop, step)):
            raise TypeError('all arguments must be integers')
        min_start, max_start = 0, 4999
        if step > 0:
            min_stop, max_stop = 1, 5000
            step_sign = 'positive'
        elif step < 0:
            min_stop, max_stop = 0, 4999
            step_sign = 'negative'
        else:
            raise ValueError('step argument must not be zero')
        if not min_start <= start <= max_start:
            msg = 'start argument out of range (must be %s..%s)'
            raise ValueError(msg % (min_start, max_start))
        if not min_stop <= stop <= max_stop:
            msg = 'stop argument out of range (must be %s..%s for %s step)'
            raise ValueError(msg % (min_stop, max_stop, step_sign))

    def __getitem__(self, index):
        length = len(self)
        if not isinstance(index, int):
            raise TypeError('sequence index must be integer, not %r'
                             % type(index).__name__)
        if not (-length <= index < length):
            raise IndexError('index out of range')
        if index >= 0:
            res = self.start + self.step*index
            return toRoman(res) if res > 0 else ''
        else:
            return self[length+index]

    def __len__(self):
        return self.stop//self.step - self.start//self.step

if __name__=='__main__':
    import doctest
    doctest.testmod()