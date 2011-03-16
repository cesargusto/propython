#!/usr/bin/env python

for i in dir(__builtins__):
    try:
        v = eval(i)
        prefix = ''
        t = type(v)
    except Exception as e:
        v = e
        prefix = '!!!'
        t = None
    print('%s\t%s\t%r\t%r' % (i, prefix, v, t))
    
    

