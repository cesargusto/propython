#!/usr/bin/env python
# coding: utf-8

from unicodedata import name

def bits(n):
    s = ''.join(reversed([str((n>>i)&1) for i in range(64)])).lstrip('0')
    while len(s) % 8:
        s = '0' + s
    return s

CHARS = u'''A Ã €'''.split()
CHARS.append(unichr(0x6c23))
CHARS.append(unichr(0x9e7e))
CHARS.append(unichr(0x1d11e))

for c in CHARS:
    utf = c.encode('utf-8')
    bytes = ' '.join([bits(ord(b)) for b in utf])
    #print '%6d %06x  %s\t%24s | %s' % (ord(c), ord(c), c, bits(ord(c)), bytes)
    print u'{0:6d} {1:06x} {2:>2s}\t{3:>24s} | {4}'.format(ord(c), ord(c), c, bits(ord(c)), bytes)
    #print name(c)

