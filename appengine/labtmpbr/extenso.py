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
    10**3: 'mil',
    10**6: 'milhão',
    10**9: 'bilhão',
    10**12: 'trilhão',
    10**15: 'quadrilhão',
    10**18: 'quintilhão',
    10**21: 'sextilhão',
    10**24: 'setilhão',
    10**27: 'octilhão',
    10**30: 'nonilhão',
    10**33: 'decilhão',
    10**36: 'undecilhão',
    10**39: 'dodecilhão',
    10**42: 'tredecilhão',
    10**45: 'quatuordecilhão',
    10**48: 'quindecilhão',
    10**51: 'sedecilhão',
    10**54: 'septendecilhão',
    10**57: 'octodecilhão',
    10**60: 'nonidecilhão',
}

limite = max(cardinais_pot1000)*1000-1

def cardinal999(n):
    assert 0<=n<1000
    if n in cardinais:
        return cardinais[n]
    else:
        pot10 = 10**int(log(n, 10))
        cabeca = n/pot10
        corpo =  n%pot10
        redondo = cabeca*pot10
        if redondo == 100:
            prefixo = 'cento'
        else:
            prefixo = cardinais[redondo]
        return prefixo + ' e ' + cardinal999(corpo)

def cardinal(n):
    if n < 1000:
        return cardinal999(n)
    else:
        # int(log(n,1000)) não tem precisão suficiente a partir de 10**14,
        # por isso a operação com str e len (dica do Leandro Lameiro)
        pot1000 = 1000**((len(str(n))-1)/3)
        cabeca = n/pot1000
        corpo =  n%pot1000
        if pot1000 == 1000 and cabeca == 1:
            prefixo = 'mil'
        else:
            try:
                prefixo = (cardinal999(cabeca) + ' ' +
                           cardinais_pot1000[pot1000])
            except KeyError:
                raise OverflowError('limite %s ultrapassado' % limite)
            if cabeca != 1:
                prefixo = prefixo.replace('ilhão', 'ilhões')
        if corpo:
            if (0<corpo<100) or (corpo < 1000 and (corpo%100)==0):
                conector = ' e '
            elif prefixo == 'mil':
                conector = ' '
            else:
                conector = ', '
            return prefixo + conector + cardinal(corpo)
        else:
            return prefixo

def teste(n, esperado):
    if cardinal(n) == esperado:
        print n,
    else:
        print '\n%s ESPERADO: %r RESPOSTA: %r' % (n, esperado, cardinal(n))

def testes():
    # primeira iteração rev. 178a5c0d55d5
    teste(0, 'zero')
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
    # quinta iteração: superando o bug da imprecisão do log, valeu Lameiro!
    teste(999999999999999,'novecentos e noventa e nove trilhões, '
                          'novecentos e noventa e nove bilhões, '
                          'novecentos e noventa e nove milhões, '
                          'novecentos e noventa e nove mil, '
                          'novecentos e noventa e nove')
    teste(10**21-1, 'novecentos e noventa e nove quintilhões, '
                    'novecentos e noventa e nove quadrilhões, '
                    'novecentos e noventa e nove trilhões, '
                    'novecentos e noventa e nove bilhões, '
                    'novecentos e noventa e nove milhões, '
                    'novecentos e noventa e nove mil, '
                    'novecentos e noventa e nove')
    # "Debt to the Penny": dívida pública dos EUA em 03/03/2011, fonte oficial:
    # http://www.treasurydirect.gov/NP/BPDLogin?application=np
    teste(14182086199057, 'quatorze trilhões, cento e oitenta e dois '
                          'bilhões, oitenta e seis milhões, cento e noventa '
                          'e nove mil e cinquenta e sete')
    # um parsec = 30856774880361360 metros, fonte:
    # http://en.wikipedia.org/wiki/Parsec
    teste(30856774880361360, 'trinta quadrilhões, oitocentos e cinquenta e '
                             'seis trilhões, setecentos e setenta e quatro '
                             'bilhões, oitocentos e oitenta milhões, trezentos '
                             'e sessenta e um mil, trezentos e sessenta')
    teste(999*10**60,'novecentos e noventa e nove nonidecilhões')
    try:
        cardinal(limite+1)
    except OverflowError:
        pass
    else:
        raise Exception('this test should raise OverflowError')
        
if __name__=='__main__':
    testes()


