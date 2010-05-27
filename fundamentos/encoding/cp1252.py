# coding: latin-1

from unicodedata import normalize, name

def unicode2ascii(u):
    return normalize('NFKD', unicode(u)).encode('ASCII','ignore')

for i in range(128,256):
    c = chr(i)
    try:
        u = c.decode('cp1252')
    except UnicodeDecodeError:
        u = '?'
        descr = 'UnicodeDecodeError'
    else:
        descr = name(u)
    #a = unicode2ascii(c) 
    a = ''
    print '%3d\t%r\t%s\t%s\t%s' % (i, c, u, a, descr)
s = 'maçã'
print len(s)
print s

