#!/usr/bin/env python

'''
The `dec2bin` function returns a binary representation of an integer::

    >>> dec2bin(0)
    '0'
    >>> dec2bin(1)
    '1'
    >>> dec2bin(10)
    '1010'
    >>> dec2bin(int('ff',16))
    '11111111'
    >>> dec2bin(int('aaaa',16))
    '1010101010101010'

The binary result may be padded with 0s to a specified length::

    >>> dec2bin(10,8)
    '00001010'
    >>> dec2bin(int('ff',16),16)
    '0000000011111111'
    
Bits may be separated at word boundaries. The default word length is 8::    
        
    >>> dec2bin(int('ff',16),16, ':')
    '00000000:11111111'
    >>> dec2bin(int('ff',16), 12, ' ')
    '0000 11111111'
    >>> dec2bin(int('aaaa',16),32,' ')
    '00000000 00000000 10101010 10101010'

A different word length may be specified::

    >>> dec2bin(10,8,':',4)
    '0000:1010'
    >>> dec2bin(int('ff',16), 12, sep=' ', word_len=4)
    '0000 1111 1111'

The recursive implementation also works. Here's a demo with large numbers::

    >>> s = dec2bin2(2**70)
    >>> s
    '10000000000000000000000000000000000000000000000000000000000000000000000'
    >>> len(s)
    71
    >>> s2 = dec2bin2(2**70-1)
    >>> s2
    '1111111111111111111111111111111111111111111111111111111111111111111111'
    >>> len(s2)
    70

The one-liner works within it's limitations::

    >>> dec2bin1(0)
    '0'
    >>> dec2bin1(2**8-1)
    '11111111'
    >>> dec2bin1(2**8)
    '100000000'
    >>> dec2bin1(2**64-1) == '1'*64
    True
    
    
'''

def dec2bin1(n):
    ''' dec2bin(n) -> n as string of bits
    
    One-liner with limitations: max width is 64, leading zeros removed. 
    '''
    return ''.join(reversed([str((n>>i)&1) for i in range(64)])).lstrip('0') or '0'
    
def dec2bin2(d):
    ''' dec2bin(n) -> n as string of bits
    
    Recursive implementation.
    '''
    if d == 0:
        return '0'
    else:
        bit = '1' if d % 2 else '0'
        return dec2bin(d/2).lstrip('0')+bit    

def dec2bin(n, width=0, sep='', word_len=8):
    ''' dec2bin(n) -> n as string of bits
    
    Result may be optionally zero-padded to a certain width, 
    and separated in words of specified length.
    '''
    if n == 0:
        return '0'
    bits = []
    while n:
        bits.insert(0, str(n&1))
        n >>= 1
    if len(bits) < width:
        bits[:0] = ['0']*(width-len(bits))
    if sep:
        for i in xrange(len(bits)-word_len,0,-word_len):
            bits.insert(i, sep)    
    return ''.join(bits)     

if __name__ == '__main__':
    import doctest
    doctest.testmod()

