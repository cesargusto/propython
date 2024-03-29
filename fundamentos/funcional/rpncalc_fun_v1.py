#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    
def analisar(expr):
    ''' devolve uma AST da expressão
         
        >>> analisar('5 2 +')
        ['+', '5', '2']
        >>> analisar('212 32 - 9 / 5 *')
        ['*', ['/', ['-', '212', '32'], '9'], '5']
        >>> analisar('212 32 - 5 9 / *')
        ['*', ['-', '212', '32'], ['/', '5', '9']]
    '''
        
    acoes = {
        '<NUM>' : lambda p,e: p.append(e),
        '<NDA>' : lambda p,e: p.append([e, p.pop(-2), p.pop()]),
    }
    return processar(expr, acoes)
    
def ast2str(ast, fmt):
    if isinstance(ast, list):
        op, a1, a2 = ast
        return fmt % dict(op=op, 
                          a1=ast2str(a1, fmt), 
                          a2=ast2str(a2, fmt))
    else:
        return str(ast)

def sexpr(expr):
    ''' converte uma expresão RPN em uma s-expression 
    
        >>> sexpr('5 2 +')
        '(+ 5 2)'
        >>> sexpr('212 32 - 5 9 / *')
        '(* (- 212 32) (/ 5 9))'
    
    '''
    ast = analisar(expr)
    return ast2str(ast, '(%(op)s %(a1)s %(a2)s)')
    
def pyexpr(expr):
    ''' converte uma expresão RPN em uma expressão Python
    
        >>> pyexpr('5 2 +')
        '(5 + 2)'
        >>> pyexpr('212 32 - 5 9 / *')
        '((212 - 32) * (5 / 9))'
    
    '''
    ast = analisar(expr)
    return ast2str(ast, '(%(a1)s %(op)s %(a2)s)')
    
    
    

if __name__=='__main__':
    import doctest
    doctest.testmod()
