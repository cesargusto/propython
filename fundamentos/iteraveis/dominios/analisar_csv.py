# coding: utf-8

from __future__ import unicode_literals

SRC = 'http://newgtlds-cloudfront.icann.org/sites/default/files/reveal/strings-1200utc-13jun12-en.csv'

import csv
import itertools

nome_arq = SRC.split('/')[-1]

pedidos = []

with open(nome_arq, 'U') as arq:
    linhas, parsear = itertools.tee(arq)
    parser = csv.DictReader(parsear)
    cabecalho = linhas.next()
    for linha in linhas:
        print linha
        pedido = parser.next()
        for chave, valor in pedido.items():
            pedido[chave] = valor.decode('utf-8')
        pedidos.append(pedido)

pedido = pedidos[0]
print pedido.keys()

for pedido in pedidos:
    print pedido['String']
