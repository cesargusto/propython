#!/usr/bin/env python

from math import pi, sqrt

PRECISAO = 0.0001

def soma_rec(termo, a, proximo, b):
    if a > b: return 0
    return termo(a) + soma_rec(termo, proximo(a), proximo, b)
    
def soma_iter(termo, a, proximo, b):
    total = 0
    while a <= b:
        total += termo(a)
        a = proximo(a)
    return total

def soma_gen(termo, a, proximo, b):
    def serie(a):
        while a <= b:
            yield termo(a)
            a = proximo(a)
    return sum(serie(a))
    
somatoria = soma_rec
#somatoria = soma_iter
somatoria = soma_gen
    
def inc(n): return n + 1

def cubo(n): return n * n * n

def soma_cubos(a, b):
    return somatoria(cubo, a, inc, b)
    
assert soma_cubos(1,10) == 3025

def soma_ints(a, b):
    return somatoria(lambda x:x, a, inc, b)
    
assert soma_ints(1,10) == 55

def dicotomia_de_zeno(a, b):
    def termo_zeno(n): return 1.0 / 2**n
    return somatoria(termo_zeno, a, inc, b)
    
assert abs(1-dicotomia_de_zeno(1, 100)) < PRECISAO
    
def soma_pi(a, b):
    def termo_pi(x):
        return 1.0 / (x * (x + 2))
    def prox_pi(x):
        return x + 4
    return somatoria(termo_pi, a, prox_pi, b)
    
if somatoria is soma_rec:
    # se b > 3988: RuntimeError: maximum recursion depth exceeded
    assert abs(pi - soma_pi(1, 3988) * 8) < 0.001 
else:
    assert abs(pi - soma_pi(1, 100000) * 8) < PRECISAO

def integral(f, a, b, dx):
    def inc_dx(x): return x + dx
    return somatoria(f, a + dx/2.0, inc_dx, b) * dx
    
assert abs(.25 - integral(cubo, 0, 1, 0.01)) < PRECISAO
assert abs((1.0/3) - integral(lambda x:x*x, 0, 1, 0.01)) < PRECISAO
assert abs((2.0/3) - integral(sqrt, 0, 1, 0.01)) < PRECISAO
assert abs(18 - integral(sqrt, 0, 9, 0.01)) < PRECISAO

def in_pot(pot): # integral de x**pot
    return lambda x:x**(pot+1)/float(pot+1)

if somatoria is soma_rec:
    # novamente, limitado pela recursão
    assert abs(in_pot(7)(2)-integral(lambda x:x**7, 0, 2, 0.01)) < 0.01
else:
    assert abs(in_pot(7)(2)-integral(lambda x:x**7, 0, 2, 0.001)) < PRECISAO

print 'OK'

