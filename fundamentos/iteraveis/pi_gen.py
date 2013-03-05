#!/usr/bin/env python
# coding: utf-8

"""
    >>> 3.1 < monte_pi(1000) < 3.2
    True
    
"""


from random import random

def monte_pi(iteracoes):
    '''calcular pi pelo método de Monte Carlo'''
    dentro = 0
    for i in range(iteracoes):
        x, y = random(), random()
        if x*x + y*y <= 1:
            dentro += 1
    return 4.0 * dentro / iteracoes
    
def monte_pi_gen():
    '''calcular pi pelo método de Monte Carlo'''
    iteracoes = dentro = 0
    while True:
        iteracoes += 1
        x, y = random(), random()
        if x*x + y*y <= 1:
            dentro += 1
        yield 4.0 * dentro / iteracoes

if __name__ == '__main__':
    pi0 = -1
    for pi in monte_pi_gen():
        print pi
        if pi < 4 and pi == pi0:
            break
        pi0 = pi

