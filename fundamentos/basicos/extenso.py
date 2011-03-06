#!/usr/bin/env python
# coding: utf-8

from math import log

cardinais = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
    100: 'cem', # cento
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seiscentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos',
    1000: 'mil',
    10**6: 'um milhão',
    10**9: 'um bilhão',
    10**12: 'um trilhão',
    10**15: 'um quadrilhão',
    10**18: 'um quintilhão'
}

def cardinal(n):
    if n in cardinais:
        return cardinais[n]
    else:
        pot10 = 10 ** int(log(n, 10)) 
        cabeca = n/pot10
        return cardinal(cabeca*pot10) + ' e ' + cardinal(n%pot10)

def teste(n, esperado):
    assert cardinal(n) == esperado, 'ESPERADO: %r RESPOSTA: %r' % (esperado, cardinal(n))
        
def testes():
    teste(1, 'um')
    teste(10, 'dez')
    teste(12, 'doze')
    teste(23, 'vinte e três')
    teste(597, 'quinhentos e noventa e sete')
    print 'OK'
    
if __name__=='__main__':
    testes()    
           
        
