# coding: utf-8

'''
Analisador simples de syslog
'''

import io
import sys
import operator

def contar_linhas(nome_arq_log):
    arq_log = io.open(nome_arq_log, encoding='utf-8')
    linhas = arq_log.readlines()
    arq_log.close()
    print len(linhas), 'linhas'

def extrair_nomes_prog(nome_arq_log, qtd_linhas=None):
    progs = {}

    arq_log = io.open(nome_arq_log, encoding='utf-8')

    for num_linha, linha in enumerate(arq_log):
        if linha[0] in ' \t':
            continue
        if 'last message repeated' in linha:
            continue
        linha = linha.rstrip()
        datahora = linha[:16]
        resto = linha[16:]
        hostname, resto = resto.split(None, 1)
        try:
            proc, resto = resto.split(':', 1)
        except ValueError:
            print 'linha sem ":"'
            print linha
            raise SystemExit

        if '[' in proc:
            prog, proc = proc.split('[', 1)
        else:
            prog = proc
        if prog in progs:
            progs[prog] += 1
        else:
            progs[prog] = 1

        if qtd_linhas is not None:
            if num_linha == qtd_linhas:
                break

    arq_log.close()

    itens = progs.items()
    # iterar pelos itens (k, v) ordenados pelo valor v
    for i, (prog, qtd) in enumerate(sorted(itens,
                            key=operator.itemgetter(1),
                            reverse=True), 1):
        print '%3d %5d %s' % (i, qtd, prog)

nome_arq_log = sys.argv[1]
#contar_linhas(nome_arq_log)
extrair_nomes_prog(nome_arq_log)
