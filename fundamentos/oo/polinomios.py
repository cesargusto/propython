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
        
    Um polinômio pode ser invocado como uma função com a variável passada como
    argumento::
        
        >>> p(3)
        -241
        
    É permitido criar um Polinomio nulo:
    
        >>> p0 = Polinomio()
        >>> p0.grau()
        0
        >>> p0(3)
        0
        
    Testes com polinomios densos::
    
        >>> p = Polinomio( *[(e, 1) for e in range(10)] )
        >>> print p
        x**9 + x**8 + x**7 + x**6 + x**5 + x**4 + x**3 + x**2 + x + 1
        >>> p(2)
        1023
        >>> p = Polinomio( *[(e, float(1)/(e+1)) for e in range(10)] )
        >>> print p
        .1*x**9 + .111*x**8 + .125*x**7 + .143*x**6 + .167*x**5 + .2*x**4 + .25*x**3 + .333*x**2 + .5*x + 1
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
        Termo(exp=100, coef=1.0)
        
    E com um termo, pode-se montar um monômio::
    
        >>> m = Polinomio(p[0])
        >>> print m
        x**100
        
    Num polinômio, todos os expoentes têm que ser inteiros não-negativos::
    
        >>> errado = Polinomio( (-1, 2), (2, 3) )
        Traceback (most recent call last):
          ...
        ValueError: O expoente tem que ser um inteiro nao-negativo (exp = -1)
        >>> errado = Polinomio( (2, 3), (1.5, 2) )
        Traceback (most recent call last):
          ...
        ValueError: O expoente tem que ser um inteiro nao-negativo (exp = 1.5)
        
    Testes com a soma de polinomios::
        
        >>> p1 = Polinomio((5, -1), (3, 2), (2, -5), (0, -7))
        >>> print p1
        -x**5 + 2*x**3 - 5*x**2 - 7
        >>> p2 = Polinomio((5, 3), (3, 4), (0, 10))
        >>> print p2
        3*x**5 + 4*x**3 + 10
        >>> print p1 + p2
        2*x**5 + 6*x**3 - 5*x**2 + 3
        
    Testes com a multiplicação de polinomios::
    
        >>> p1 = Polinomio((2, 3), (1, -9), (0, 5))
        >>> print p1
        3*x**2 - 9*x + 5
        >>> p1(3)
        5
        >>> p2 = Polinomio((3, 2))
        >>> print p2
        2*x**3
        >>> p2(3)
        54
        >>> p3 = p1 * p2
        >>> print p3
        6*x**5 - 18*x**4 + 10*x**3
        >>> p3(3)
        270

'''

def fmt_num(n):
    if isinstance(n, (int, long)):
        return str(n)
    res = ('%.3f' % n).strip('0')
    return res if res[-1] != '.' else res + '0'
    
class Polinomio(object):
    
    def __init__(self, *termos):
        # `if coef` é para ignorar termos de coeficiente zero
        self.termos = [Termo(exp, coef) for exp, coef in termos if coef]
        self.termos.sort(reverse=True)
        
    def grau(self):
        return self.termos[0].exp if self.termos else 0

    def __call__(self, x):
        return sum(coef*x**exp for exp, coef in self.termos)
        
    def __getitem__(self, i):
        return self.termos[i]
        
    def __add__(self, outro):
        assert isinstance(outro, Polinomio)
        novo = dict( ((t.exp, t) for t in self.termos) )
        for termo in outro.termos:
            termo_correspondente = novo.setdefault(termo.exp, Termo(termo.exp, 0))
            termo_correspondente += termo
        return Polinomio(*novo.values())
        
    def __mul__(self, outro):
        assert isinstance(outro, Polinomio)
        novo = Polinomio()
        for termo in self.termos:
            parcial = Polinomio(*[termo*t2 for t2 in outro.termos])
            novo += parcial
        return novo
        
    def __str__(self):
        s = ' + '.join(str(t) for t in self.termos)
        return s.strip().replace('+ -', '- ')
        
class Termo(object):
    exp = 0
    coef = 1
    
    def __init__(self, exp, coef):
        try:
            exp_i = int(exp) # ValueError pode ser levantado aqui também
            if exp_i != exp or exp_i < 0:
                raise ValueError()
        except ValueError:
            msg = 'O expoente tem que ser um inteiro nao-negativo '
            raise ValueError(msg + '(exp = %r)' % exp)
        self.exp = exp_i
        self.coef = coerce(coef, 1)[0]
              
    def __getitem__(self, i):
        return (self.exp, self.coef)[i]
        
    def __cmp__(self, t):
        return cmp(tuple(self), tuple(t))
        
    def __add__(self, outro):
        'somar este termo a outro, devolvendo um novo'
        assert isinstance(outro, Termo)
        assert self.exp == outro.exp
        return Termo(self.exp, self.coef+outro.coef)

    def __iadd__(self, outro):
        'somar outro termo modificando este (in-place addition +=)'
        assert isinstance(outro, Termo)
        assert self.exp == outro.exp
        self.coef += outro.coef
     
    def __mul__(self, outro):
        'multiplicar este termo com outro, devolvendo um novo'
        assert isinstance(outro, Termo)
        return Termo(self.exp+outro.exp, self.coef*outro.coef)

    def __repr__(self):
        return 'Termo(exp=%s, coef=%s)' % (self.exp, self.coef)   
           
    def __str__(self):
        if self.exp == 0:
            s = '1'
        elif self.exp == 1:
            s = 'x'
        else:
            s = 'x**' + fmt_num(self.exp)
        if abs(int(self.coef)) != 1:
            s = fmt_num(self.coef) + '*' + s if self.exp else fmt_num(self.coef)
        elif int(self.coef) == -1:
            s = '-' + s
        return s
        
def smoke_test():
        p1 = Polinomio((2, 3), (1, -9), (0, 5))
        print p1
        p2 = Polinomio((3, 2))
        print p2
        print p1 * p2
        print 'OK'
   
if __name__=='__main__':
    smoke_test()
    import doctest
    doctest.testmod()    
