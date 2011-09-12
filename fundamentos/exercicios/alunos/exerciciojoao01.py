#!/usr/bin/env python

>>> v = [7, 2, 8, 3, 1, 5]
>>> s = 'brasileiro'
>>> t = ('uva', 'ave', 'ovo')
>>> v
[7, 2, 8, 3, 1, 5]
>>> s
'brasileiro'
>>> t
('uva', 'ave', 'ovo')
>>> v[2]
8
>>> s[-1]
'o'
>>> t[0]
'uva'
>>> s[3]
's'
>>> 
>>> 
>>> 
>>> v[-1]
5
>>> t[-2]
'ave'
>>> s[-4]
'e'
>>> 
>>> 
>>> s[1:4]
'ras'
>>> v[:3]
[7, 2, 8]
>>> s[:-4]
'brasil'
>>> s[6:]
'eiro'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> m= range(10)
>>> m
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> m[1:6]
[1, 2, 3, 4, 5]
>>> m[1:6:2]
[1, 3, 5]
>>> s[::2]
'baier'
>>> m[::-2]
[9, 7, 5, 3, 1]
>>> s[::-3]
'oesb'
>>> 
>>> 8 in v
True
>>> 9 in v
False
>>> 'a' in t
False
>>> 'ave' in t
True
>>> 'a' in s
True
>>> 'argentino' not in s
True
>>> 
>>> 
>>> max(v)
8
>>> min(s)
'a'
>>> min(v[:4])
2
>>> max(t)
'uva'
>>> len(v)
6
>>>

if__name=='__main__':
>>> import doctest
>>> doctest.REPORT_ONLY_FIRST_FAILURE
512
>>> doctest.NORMALIZE_WHITESPACE
4
>>> doctest.testmod
<function testmod at 0x02C1D430>
>>> 