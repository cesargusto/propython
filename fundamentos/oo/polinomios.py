#!/usr/bin/env python
# coding: utf-8

'''
    Para instanciar um polinômio, forneça como argumentos todos os pares de 
    (expoente, coeficiente). Por exemplo, para -x**5 + 2*x**3 - 5*x**2 - 7::
    
        >>> p = Polinomio((5, -1), (3, 2), (2, -5), (0, -7))
        >>> print p
        -x**5 + 2*x**3 - 5*x**2 - 7
        >>> p.grau()
        5
        >>> p(3)
        -241
        
    Testes com polinomios densos::
    
        >>> p = Polinomio( *[(e, 1) for e in range(10)] )
        >>> print p
        x**9 + x**8 + x**7 + x**6 + x**5 + x**4 + x**3 + x**2 + x**1 + 1
        >>> p(2)
        1023
        >>> p = Polinomio( *[(e, float(1)/(e+1)) for e in range(10)] )
        >>> print p
        .1*x**9 + .111*x**8 + .125*x**7 + .143*x**6 + .167*x**5 + .2*x**4 + .25*x**3 + .333*x**2 + .5*x**1 + 1
        >>> print '%0.3f' % p(3.1)
        4141.700
        >>> from math import pi
        >>> print '%0.3f' % p(-pi)
        -2203.378

    Teste com polinomio esparso::

        >>> p = Polinomio( *[(e*10, 1) for e in range(1, 11)] )
        >>> print p
        x**100 + x**90 + x**80 + x**70 + x**60 + x**50 + x**40 + x**30 + x**20 + x**10
        >>> print p(2) # OO.org Calc: 1268889750375080000000000000000 
        1268889750375080065623288448000
        >>> print float(p(2)) # OO.org Calc: 1.26888975038E+30
        1.26888975038e+30
        
    O mesmo polinomio acima, com coeficientes float::
        
        >>> p = Polinomio( *[(e*10, 1.0) for e in range(1, 11)] )
        >>> print p(2)
        1.26888975038e+30
        
    É possível acessar cada termo do polinômio (o termo zero é o de maior
    expoente)::
    
        >>> p[0]    
        (100, 1.0)
        
    E com um termo, pode-se montar um monômio::
    
        >>> m = Polinomio(p[0])
        >>> print m
        x**100
        
    Num polinômio, todos os expoentes têm que ser inteiros não-negativos::
    
        >>> errado = Polinomio( (-1, 2), (2, 3) )
        Traceback (most recent call last):
          ...
        ValueError: Os expoentes tem que ser inteiros nao-negativos (exp = -1)
        >>> errado = Polinomio( (2, 3), (1.5, 2) )
        Traceback (most recent call last):
          ...
        ValueError: Os expoentes tem que ser inteiros nao-negativos (exp = 1.5)
        
'''

def fmt_num(n):
    if isinstance(n, (int, long)):
        return str(n)
    res = ('%.3f' % n).strip('0')
    return res if res[-1] != '.' else res + '0'
    
class Polinomio(object):
    
    def __init__(self, *termos):
        self.termos = []
        for exp, coef in termos:
            try:
                exp_i = int(exp) # ValueError pode ser levantado aqui também
                if exp_i != exp or exp_i < 0:
                    raise ValueError()
            except ValueError:
                msg = 'Os expoentes tem que ser inteiros nao-negativos '
                raise ValueError(msg + '(exp = %r)' % exp)
            if coef: # se o coeficiente é zero, ignorar termo
                self.termos.append( (exp_i, coef) )    
        self.termos.sort(reverse=True)
        
    def __str__(self):
        p = []
        for exp, coef in self.termos:
            if not exp:
                t = '1'
            else:
                t = 'x**' + fmt_num(exp)
            if abs(int(coef)) != 1:
                fmt_coef = '%d' if isinstance(coef, (int, long)) else '%f'
                t = fmt_num(coef) + '*' + t if exp else fmt_num(coef)
            elif int(coef) == -1:
                t = '-' + t
            p.append(' %s '%t)    
        s = '+'.join(p)
        s = s.replace('+ -', '- ')
        return s.strip()
        
    def grau(self):
        if len(self.termos) == 0:
            return 0
        else:    
            exp, coef = self.termos[0]
            return exp

    def __call__(self, x):
        return sum(coef*x**exp for exp, coef in self.termos)
        
    def __getitem__(self, i):
        return self.termos[i]
        
       
    
    
if __name__=='__main__':
    import doctest
    doctest.testmod()    
    

