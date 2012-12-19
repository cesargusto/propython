# coding: utf-8

'''
Encontrar menor e maior valor positivo representado em um float
'''

f_1 = None
f_2 = None
i = 0
while True:
    s = '1'+i*'0'
    f = float(s)
    if f == f_1:
        print i
        print s
        print f_1
        print repr(f_2)
        break
    f_2 = f_1
    f_1 = f
    i += 1
print '----'
i = 0
while True:
    s = '1'+i*'0'
    f = 1./float(s)
    if f == f_1:
        print i
        print s
        print f_1
        print repr(f_2)
        break
    f_2 = f_1
    f_1 = f
    i += 1
