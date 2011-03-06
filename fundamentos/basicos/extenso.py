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
}

cardinais_pot1000 = {
    1: 'mil',
    2: 'milhão',
    3: 'bilhão',
    4: 'trilhão',
    5: 'quadrilhão',
    6: 'quintilhão'
}

def cardinal999(n):
    assert 0<=n<1000
    if n in cardinais:
        return cardinais[n]
    else:
        casas = int(log(n, 10))
        cabeca = n/(10**casas)
        corpo = n%(10**casas)
        redondo = cabeca*(10**casas)
        if redondo == 100:
            prefixo = 'cento'
        else:
            prefixo = cardinais[redondo]
        return prefixo + ' e ' + cardinal(corpo)

def cardinal(n):
    assert 0<=n<10**14 # 999999999999999 exceeds max recursion. why?
    miles = int(log(n,1000))
    if miles == 0:
        return cardinal999(n)
    else:
        cabeca = n/(1000**miles)
        corpo =  n%(1000**miles)
        if miles == 1 and cabeca == 1:
            prefixo = 'mil'
        else:
            prefixo = cardinal999(cabeca) + ' ' + cardinais_pot1000[miles]
            if cabeca != 1:
                prefixo = prefixo.replace('ilhão', 'ilhões')
        if corpo:
            if (0<corpo<100) or (corpo < 1000 and (corpo%100)==0):
                return prefixo + ' e ' + cardinal(corpo)
            elif prefixo == 'mil':
                return prefixo + ' ' + cardinal(corpo)
            else:
                return prefixo + ', ' + cardinal(corpo)
        else:
            return prefixo

def teste(n, esperado):
    if cardinal(n) == esperado:
        print n,
    else:
        print '\n%s ESPERADO: %r RESPOSTA: %r' % (n, esperado, cardinal(n))

def testes():
    # primeira iteração rev. 178a5c0d55d5
    teste(1, 'um')
    teste(10, 'dez')
    teste(12, 'doze')
    teste(23, 'vinte e três')
    teste(42, 'quarenta e dois')
    teste(597, 'quinhentos e noventa e sete')
    # segunda iteração, "cem, cento..." rev. f13befa3b1c2
    teste(100, 'cem')
    teste(101, 'cento e um')
    teste(150, 'cento e cinquenta')
    teste(198, 'cento e noventa e oito')
    # terceira iteração
    teste(1000, 'mil')
    teste(1001, 'mil e um')
    teste(1035, 'mil e trinta e cinco')
    teste(1100, 'mil e cem')
    teste(1110, 'mil cento e dez')
    teste(1189, 'mil cento e oitenta e nove')
    teste(1200, 'mil e duzentos')
    teste(1209, 'mil duzentos e nove')
    teste(1235, 'mil duzentos e trinta e cinco')
    teste(2000, 'dois mil')
    teste(2001, 'dois mil e um')
    teste(1000000, 'um milhão')
    teste(1000001, 'um milhão e um')
    teste(1000722, 'um milhão, setecentos e vinte e dois')
    teste(1722000, 'um milhão, setecentos e vinte e dois mil')
    teste(2000000, 'dois milhões')
    teste(2000001, 'dois milhões e um')
    teste(2000722, 'dois milhões, setecentos e vinte e dois')
    teste(2722000, 'dois milhões, setecentos e vinte e dois mil')
    teste(987654321, 'novecentos e oitenta e sete milhões, seiscentos '
                     'e cinquenta e quatro mil, trezentos e vinte e um')
    teste(99999999999999, 'noventa e nove trilhões, '
                          'novecentos e noventa e nove bilhões, '
                          'novecentos e noventa e nove milhões, '
                          'novecentos e noventa e nove mil, '
                          'novecentos e noventa e nove')
    #teste(999999999999999,'novecentos e noventa e nove trilhões, ...')
    '''
      File "./extenso.py", line 90, in cardinal
        return prefixo + ', ' + cardinal(corpo)
      File "./extenso.py", line 90, in cardinal
        return prefixo + ', ' + cardinal(corpo)
      File "./extenso.py", line 90, in cardinal
        return prefixo + ', ' + cardinal(corpo)
      File "./extenso.py", line 81, in cardinal
        prefixo = cardinal999(cabeca) + ' ' + cardinais_pot1000[miles]
      File "./extenso.py", line 56, in cardinal999
        assert 0<=n<1000
    RuntimeError: maximum recursion depth exceeded in cmp
    '''
if __name__=='__main__':
    testes()


