#!/usr/bin/env python
# coding: utf-8

cardinais = {     0: 'zero',              
    1: 'um',     11: 'onze',      10: 'dez',       100: 'cem',
    2: 'dois',   12: 'doze',      20: 'vinte',     200: 'duzentos',
    3: 'três',   13: 'treze',     30: 'trinta',    300: 'trezentos',
    4: 'quatro', 14: 'quatorze',  40: 'quarenta',  400: 'quatrocentos',
    5: 'cinco',  15: 'quinze',    50: 'cinquenta', 500: 'quinhentos',
    6: 'seis',   16: 'dezesseis', 60: 'sessenta',  600: 'seiscentos',
    7: 'sete',   17: 'dezessete', 70: 'setenta',   700: 'setecentos',
    8: 'oito',   18: 'dezoito',   80: 'oitenta',   800: 'oitocentos',
    9: 'nove',   19: 'dezenove',  90: 'noventa',   900: 'novecentos',
}

def cardinal999(n):
    assert 0 <= n < 1000
    if n in cardinais:
        return cardinais[n]
    else:
        pot10 = len(str(n))-1
        cabeca, corpo = divmod(n, 10**pot10)
        redondo = cabeca * 10**pot10
        if redondo == 100:
            prefixo = 'cento'
        else:
            prefixo = cardinais[redondo]
        return prefixo + ' e ' + cardinal999(corpo)

cardinais_pot1000 = '''mil milhão bilhão trilhão quadrilhão quintilhão
    sextilhão setilhão octilhão nonilhão decilhão undecilhão dodecilhão 
    tredecilhão quatuordecilhão quindecilhão sedecilhão septendecilhão 
    octodecilhão nonidecilhão'''.split()

limite = 1000**(len(cardinais_pot1000)+1)

def cardinal(n):
    if n < 1000:
        return cardinal999(n)
    else:
        pot1000 = (len(str(n))-1)/3
        cabeca, corpo = divmod(n, 1000**pot1000)
        if pot1000 == 1 and cabeca == 1:
            prefixo = 'mil'
        else:
            try:
                prefixo = (cardinal999(cabeca) + ' ' +
                           cardinais_pot1000[pot1000-1])
            except IndexError:
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

if __name__=='__main__':
    import sys
    if len(sys.argv) == 2:
        print cardinal(int(sys.argv[1]))
    else:
        while True:
            n = raw_input('digite um número: ')
            if not n: break
            try:
                n = int(n)
                print cardinal(n)
            except ValueError:
                print n,'?'