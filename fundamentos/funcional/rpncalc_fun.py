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
    def erro(p, e):
        raise ValueError('operador desconhecido: %s' % e)

    acoes = {
        '<NUM>' : lambda p,e: p.append(float(e)),
        '+' : lambda p,e: p.append(p.pop()+p.pop()),
        '-' : lambda p,e: p.append(p.pop(-2)-p.pop()),
        '*' : lambda p,e: p.append(p.pop()*p.pop()),
        '/' : lambda p,e: p.append(p.pop(-2)/p.pop()),
        '<NDA>' : erro
    }
    return processar(expr, acoes)    

def processar(expr, acoes):
    pilha = []
    for elemento in expr.split():
        tipo = '<NUM>' if numero(elemento) else '<INDEF>'
        acao = acoes.get(tipo) or acoes.get(elemento) or acoes.get('<NDA>')
        acao(pilha, elemento)
    return pilha.pop()
    
if __name__=='__main__':
    import sys
    if len(sys.argv) < 2:
        print 'modo de usar: %s "<expressao-rpn>"' % __file__
        print '  onde <expressao-rpn> segue a forma <arg1> <arg2> <op>'
        print '  por exemplo: 6 7 *'
        sys.exit()

    expr = ' '.join(sys.argv[1:])
    # permitir uso de x no lugar de *, evitando ter que colocar ""
    expr = expr.replace('x', '*') 
    print calcular(expr)





