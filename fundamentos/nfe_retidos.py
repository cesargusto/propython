#!/usr/bin/env python3
# coding: utf-8

import sys
from decimal import Decimal, InvalidOperation

def retencoes(total):
    '''devolve tupla (irrf, lei10833, liquido)'''

    # http://www.receita.fazenda.gov.br/legislacao/ins/2012/in12342012.htm
    # § 6 º Fica dispensada a retenção de valor inferior a R$ 10,00 (dez reais)
    irrf = Decimal('0.015') * total
    if irrf < 10:
        irrf = 0

    # http://www.receita.fazenda.gov.br/legislacao/leis/2003/lei10833.htm
    # § 3º É dispensada a retenção para pagamentos de valor
    #      igual ou inferior a R$ 5.000,00 (cinco mil reais)
    if total > Decimal('5000'):
        lei10833 = Decimal('0.0465') * total
    else:
        lei10833 = 0

    return (irrf, lei10833, total - irrf - lei10833)

def fmt_moeda(valor, sep_mil='.', sep_dec=','):
    """
        >>> fmt_moeda(1)
        '1,00'
        >>> fmt_moeda(123.45)
        '123,45'
        >>> fmt_moeda(1234.56)
        '1.234,56'
        >>> fmt_moeda(12345.67)
        '12.345,67'
        >>> fmt_moeda(123456.78)
        '123.456,78'
        >>> fmt_moeda(1234567.89)
        '1.234.567,89'

    """
    res = format(valor, '0.2f')
    #res = str(valor)
    if sep_dec != '.':
        res = res.replace('.', sep_dec)
    if sep_dec not in res:
        res += sep_dec
    if sep_mil:
        inteiros, decimais = res.split(sep_dec)
        milhares = []
        while inteiros:
            milhares.append(inteiros[-3:])
            inteiros = inteiros[:-3]
        res = sep_mil.join(reversed(milhares)) + sep_dec + decimais
    return res

# from: http://docs.python.org/2/library/decimal.html
# 9.4. decimal — Decimal fixed point and floating point arithmetic
# 9.4.7. Recipes

def moneyfmt(value, places=2, curr='', sep=',', dp='.',
             pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop
    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')
    build(dp)
    if not digits:
        build('0')
    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))

total = 0
if len(sys.argv) == 2:
    try:
        total = Decimal(sys.argv[1])
    except InvalidOperation:
        total = 0

while not total:
    try:
        total = Decimal(input('Valor total da NF: '))
    except InvalidOperation:
        print('Valor inválido.')

irrf, lei10833, liquido = retencoes(total)

# fmt_moeda = moneyfmt

print('Valor total da nota fiscal = '+ fmt_moeda(total))

if irrf:
    msg = '- IRRF (Imposto de Renda Retido na Fonte) 1,5% = '
    print(msg + fmt_moeda(irrf))

if lei10833:
    msg = '- Retenção Lei 10833/2003 (PIS/Cofins/CSLL) 4,65% = '
    print(msg + fmt_moeda(lei10833))

print('Valor líquido a depositar = '+ fmt_moeda(liquido))


"""
com o valor 10930 o resultado foi:

Valor total da nota fiscal = 10.930,00
- IRRF (Imposto de Renda Retido na Fonte) 1,5% = 163,95
- Retenção Lei 10833/2003 (PIS/Cofins/CSLL) 4,65% = 508,24
Valor líquido a depositar = 10.257,80

Porém no Google Spreadsheet os descontos foram:
163.95
508.25

Usar moneyfmt não resolveu o problema...

"""
