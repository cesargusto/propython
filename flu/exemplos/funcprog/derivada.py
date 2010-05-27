#!/usr/bin/env python

# http://mathworld.wolfram.com/Derivative.html

from math import exp, pi, sin, cos

EPSILON = 0.00001
PRECISAO = EPSILON * 100

def derivada_v0(f, dx=EPSILON):
    def g(x): 
        return (f(x+dx) - f(x)) / float(dx)
    return g

def derivada(f, dx=EPSILON):
    return lambda x: (f(x+dx) - f(x)) / float(dx)

def k(x): return 1
assert abs(0-derivada(k)(1)) < PRECISAO

def ident(x): return x
assert abs(1-derivada(ident)(1)) < PRECISAO

for x in xrange(-10,10):
    assert abs(1-exp(x)/(derivada(exp)(x))) < PRECISAO

def pot(n):
    return lambda x: x**n

def deriv_pot(n):
    return lambda x: n*(x**(n-1))

for x in xrange(-10,10):
    for i in xrange(-10,10):
        try:
            if abs(x) < PRECISAO: continue
            if abs(deriv_pot(i)(x)) < PRECISAO: continue
            assert abs(1-(deriv_pot(i)(x))/derivada(pot(i))(x)) < PRECISAO
        except AssertionError:
            print x, i
            print deriv_pot(x)(i)
            print derivada(pot(x))(i)

for i in xrange(101):
    x = i * pi / 100.0
    assert abs(cos(x)-derivada(sin)(x)) < PRECISAO
    assert abs(-sin(x)-derivada(cos)(x)) < PRECISAO



