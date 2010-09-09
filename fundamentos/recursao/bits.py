#!/usr/bin/env python

def bits(n):
    bit = str(n % 2)
    return bit if n < 2 else bits(n/2) + bit
        
if __name__=='__main__':
    for i in xrange(16):
        print '%2d %x %4s' % (i, i, bits(i))
        
