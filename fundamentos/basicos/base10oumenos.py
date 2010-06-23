#!/usr/bin/env python
# coding: utf-8

def reprbase(n, base):
    ''' devolve a representação do valor `n` na `base` '''
    assert base <= 10 # para bases maiores, é preciso tratar res como string
    res = 0
    pot = 0
    while n:
        n, d = divmod(n, base)
        res += 10**pot * d # estamos abusando dos dígitos decimais aqui
        pot += 1
    return res # este resultado é um int que "parece" o número na `base`
               # por exemplo, 9 em base 2 sai como 1001, mas não é mil-e-um!!!
               
if __name__=='__main__':
    for i in range(10):
        print '%2d %10d' % (i, reprbase(i, 2))

