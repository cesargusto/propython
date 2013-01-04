# coding: utf-8

import io
import csv

with io.open('editores.txt', encoding='utf-8') as opcoes_arq:
    opcoes = set(lin.strip() for lin in opcoes_arq)

# csv.reader não pode ser usado com with pois não implementa __exit__
# csv.reader também não aceita arquivos abertos com io.open; só entende str de bytes
planilha = csv.reader(open('planilha.csv'))

ct_ide1 = {op:0 for op in opcoes}
ct_os = {}
ct_ide2 = {}

for i, lin in enumerate(planilha):
    if i == 0:
        continue
    lin = [s.decode('utf-8') for s in lin]
    data, ide1, os, ide2 = lin
    ct_os[os] = ct_os.get(os, 0) + 1
    if ide1 not in opcoes:
        ide1 += ' *'  # marcar opcao registrada em "outros"
    ct_ide1[ide1] = ct_ide1.get(ide1, 0) + 1
    if not ide2.strip():
        ide2 = u'(não informado)'
    for ide in ide2.split(','):
        ide = ide.strip()
        ct_ide2[ide] = ct_ide2.get(ide, 0) + 1

total = i  # a primeira linha é o cabeçalho

def relatorio(dic_dados, titulo=''):
    listagem = [(qtd, nome) for nome, qtd in dic_dados.items()]
    if titulo:
        print '\n' + '-'*len(titulo)
        print titulo.encode('utf-8')
        print '-'*len(titulo) + '\n'
    for qtd, nome in sorted(listagem, reverse=True):
        pct = qtd * 100. / total
        print u'{:3d}\t{:4.1f}%\t{}'.format(qtd, pct, nome).encode('utf-8')

relatorio(ct_os, u'Sistema Operacional de Desenvolvimento')
relatorio(ct_ide1, u'Editor/IDE Principal')
relatorio(ct_ide2, u'Editor/IDE Secundário')


