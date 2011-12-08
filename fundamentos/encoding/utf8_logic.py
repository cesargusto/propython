

'''
http://tools.ietf.org/html/rfc3629
'''

import sys

ranges = [0x007F, 0x07FF, 0xFFFF, 0x10FFFF]

def bytes_needed(code):
    for i, range in enumerate(ranges):
        if code <= range:
            return i+1
    raise ValueError('Code out of range')

def utf8(code):
    needed = bytes_needed(code)
    work_code = code
    if needed == 1:
        res = [code]
    else:
        bytes = []
        prefix = prefix_mask = 128
        for b in range(needed-1):
            bytes.insert(0, (work_code&63)|128)
            prefix_mask >>= 1
            prefix += prefix_mask
            work_code /= 64
        res = [prefix|work_code] + bytes
    assert unichr(code).encode('utf-8') == ''.join([chr(b) for b in res])
    return res

def display(code):
    needed = bytes_needed(code)
    bytes = utf8(code)
    utf_bits = ' '.join(['{0:08b}'.format(b) for b in bytes])
    print '{0:8x} {1}   {2}'.format(code, needed, utf_bits)

'''
for range_ in ranges:
    for i in range(-1,2):
        code = range_+i
        if code > sys.maxunicode:
            break
        display(code)
'''
for code in range(sys.maxunicode+1):
    display(code)


