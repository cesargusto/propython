#!/usr/bin/env python
# coding: utf-8

''' Exemplo de calculadora RPN

    Inspirado em exemplo de `Higher Order Perl`, by Mark J. Dominus
    Chapter 3, p.54-58. PDF disponível em: http://hop.perl.plover.com/

    >>> calcular('5 2 +')
    7.0
    >>> calcular('5 2 -')
    3.0
    >>> calcular('-5 2 *')
    -10.0
    >>> calcular('5 2 /')
    2.5
    >>> calcular('212 32 - 9 / 5 *')
    100.0
    >>> calcular('212 32 - 5 9 / *')
    100.0
'''

def numero(s):
    try:
        float(s)
        return True
    except ValueError:
        return False    

def calcular(expr):
    pilha = []
    for parte in expr.split():
        if numero(parte):
            pilha.append(float(parte))
        elif parte == '+':
            pilha.append(pilha.pop()+pilha.pop())
        elif parte == '-':
            pilha.append(pilha.pop(-2)-pilha.pop())
        elif parte == '*':
            pilha.append(pilha.pop()*pilha.pop())
        elif parte == '/':
            pilha.append(pilha.pop(-2)/pilha.pop())
        else:
            raise ValueError('operador desconhecido: %s' % parte)
    return pilha.pop()

if __name__=='__main__':
    import doctest
    doctest.testmod()
