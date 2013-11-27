#!/usr/bin/env python
# coding: utf-8

'''a idéia era mostrar que o cálculo do fatorial poderia
ser acelerado via programação dinâmica, usando um cache;
pena que não acelerou nada...'''

def fabricar_fatorial():
    cache = {}


def fatorial(n):
    if n < 2:
        return 1
    else:
        return n*fatorial(n-1)

cache = {}

def fat_cache(n):
    valor = 1
    for i in range(2,n+1):
        valor = cache.setdefault(i,i*valor)
    return valor

def crono(nome_func, *args):
    cmd = '%s(%s)' % (nome_func, ','.join([repr(a) for a in args]))
    prep = 'from __main__ import %s, cache' % nome_func
    t = Timer(cmd, prep)
    print(cmd, '->', min(t.repeat(3,100000)))

if __name__=='__main__':
    from timeit import Timer
    crono('fatorial', 10)
    crono('fatorial', 20)
    crono('fatorial', 30)
    crono('fat_cache', 10)
    crono('fat_cache', 20)
    crono('fat_cache', 30)


