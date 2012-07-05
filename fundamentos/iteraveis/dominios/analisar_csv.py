# coding: utf-8

from __future__ import unicode_literals

SRC = 'http://newgtlds-cloudfront.icann.org/sites/default/files/reveal/strings-1200utc-13jun12-en.csv'

import csv
import itertools
from operator import itemgetter

def contar_linhas(arq):
    qt = 0
    for lin in arq:
        qt += 1
    return qt

def parsear_linhas(arq):
    pedidos = []
    parser = csv.DictReader(arq)
    for pedido in parser:
        pedidos.append(pedido)
    return pedidos

def listar_regioes(arq):
    pedidos = parsear_linhas(arq)
    return [ped['Region'] for ped in pedidos]

def ordenar_por_regiao(arq):
    pedidos = parsear_linhas(arq)
    return sorted(pedidos, key=itemgetter('Region'))

def strings_por_regiao(arq):
    ordenados = ordenar_por_regiao(arq)
    lotes_regioes = itertools.groupby(ordenados, itemgetter('Region'))
    return [(chave, len(list(lote))) for chave, lote in lotes_regioes]

def relatorio_regional():
    import sys
    for regiao, qtd in strings_por_regiao(open(sys.argv[1], 'U')):
        print '{0:3}\t{1:4}'.format(regiao, qtd)

if __name__=='__main__':
    relatorio_regional()
