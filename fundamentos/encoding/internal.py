#/usr/bin/env python
# coding: utf-8

import sys
import codecs

uni = u'avião'

print('{0:8} {0:8x}'.format(sys.maxunicode))

encodings = ['cp1252', 'utf-8']

for encoding in encodings:
    nome_arq = 'internal-%s.dat' % encoding
    with codecs.open(nome_arq,'wb', encoding) as saida:
        saida.write(uni)
