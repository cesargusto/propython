# coding: utf-8

from nose import with_setup
from operator import itemgetter

import StringIO

from analisar_csv import *

FIXTURE_DATA = open('saida.txt').read()
fixture = None

def setup():
    global fixture 
    fixture = StringIO.StringIO(FIXTURE_DATA)
    #fixture.seek(0)

@with_setup(setup)
def teste_contar_linhas():
    assert contar_linhas(fixture) == 24

@with_setup(setup)
def teste_parsear_linhas_sem_erro():
    ''' resulta 23 porque a primeira é cabeçalho'''
    qt_registros = len(parsear_linhas(fixture))
    assert qt_registros == 23, str(qt_registros)

@with_setup(setup)
def teste_listar_regioes():
    ''' resulta 23 porque a primeira é cabeçalho'''
    regioes = listar_regioes(fixture)
    assert set(regioes) == set(['NA', 'AP', 'EUR']), repr(set(regioes))

@with_setup(setup)
def teste_ordenar_por_regiao():
    ''' resulta 23 porque a primeira é cabeçalho'''
    pedidos = ordenar_por_regiao(fixture)
    ordenada = pedidos[:]
    ordenada.sort(key=itemgetter('Region'))
    assert ordenada == pedidos, 'ordem diferente'

@with_setup(setup)
def teste_strings_por_regiao():
    strings_regiao = strings_por_regiao(fixture)
    esperado = [('AP', 1),
                ('EUR', 13),
                ('NA', 9)]
    assert strings_regiao == esperado, repr(strings_regiao)








