#!/usr/bin/env python
# coding: utf-8

'''
Explorando a codificação UTF-8

Referência: 
RFC-3629 - UTF-8, a transformation format of ISO 10646
http://www.rfc-editor.org/rfc/rfc3629.txt
'''

from unicodedata import name
from bits import dec2bin

def unicode2utf8bits(s):
    bits = dec2bin(ord(s))
    if len(bits) <= 7:
        return '0'*(8-len(bits))+bits
    elif len(bits) <= 11:
        bits = '0'*(11-len(bits))+bits
        return '110 ' + bits[:5] + ' 10 ' + bits[5:]
    elif len(bits) <= 16:
        bits = '0'*(16-len(bits))+bits
        return '1110 ' + bits[:4] + ' 10 ' + bits[4:10] + ' 10 ' + bits[10:] 
    elif len(bits) <= 21:
        bits = '0'*(21-len(bits))+bits
        return '11110 ' + bits[:3] + ' 10 ' + bits[3:9] + ' 10 ' + bits[9:15] + ' 10 ' + bits[15:] 

amostra = list(u'1AaÃãÇÉ')

amostra.append(u'\u06bf') # ARABIC LETTER TCHEH WITH DOT ABOVE
amostra.append(u'\u0d0b') # MALAYALAM LETTER VOCALIC R
amostra.append(u'\u2620') # SKULL AND CROSSBONES
amostra.append(u'\u4df1') # HEXAGRAM FOR THE CAULDRON
amostra.append(u'\u6c23') # CJK UNIFIED IDEOGRAPH-6C23

for c in amostra:
    nibbles = dec2bin(ord(c),sep=' ', word_len=4)
    bits = dec2bin(ord(c))
    utf8bits = unicode2utf8bits(c)
    utf8 = ' '.join(repr(b)[3:5] for b in c.encode('utf-8'))
    print '%04x %2d %18s | %-29s %s %s %s' % (ord(c), len(bits), nibbles, utf8bits, utf8, c, name(c))
    
           
        
