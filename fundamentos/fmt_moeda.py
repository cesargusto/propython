
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


def fmt_moeda(valor, sep_mil='.', sep_dec=','):
    res = format(valor, '0.2f')
    if sep_dec != '.':
        res = res.replace('.', sep_dec)
    if sep_mil:
        inteiros, decimais = res.split(sep_dec)
        milhares = []
        while inteiros:
            milhares.append(inteiros[-3:])
            inteiros = inteiros[:-3]
        res = sep_mil.join(reversed(milhares)) + sep_dec + decimais
    return res
        