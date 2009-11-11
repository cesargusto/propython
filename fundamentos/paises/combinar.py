#!/usr/bin/env python
# coding: utf-8

idiomas = ['pt-br', 'es', 'en']
paises = {}

for lin in open('list-en1-semic-3.txt'):
    lin = lin.strip()
    partes = lin.split(';')
    if len(partes) != 2: continue
    descr, cc = partes
    if cc.isalpha():
        paises[cc] = {'ISO':descr.decode('iso-8859-15')}

for idioma in idiomas:
    for lin in open('%s.txt' % idioma):
        lin = lin.decode('utf-8')
        lin = lin.replace(u'--',u'')
        lin = lin.strip()
        partes = lin.split(u'\t')
        if len(partes) != 2: continue
        cc, descr = partes
        if cc in paises:
            paises[cc][idioma] = descr

saida = open('paises.php', 'w')
saida.write('<?php\n')
saida.write('array(\n')
linhas = []
for cc in sorted(paises):
    miolo = []
    for idioma in idiomas:
        descr = paises[cc].get(idioma, paises[cc]['ISO'])
        descr = descr.encode('utf-8')
        miolo.append('"%s"=>"%s"' % (idioma, descr))
    linhas.append('    "%s"=>array(%s)' % (cc, ','.join(miolo)))
saida.write(',\n'.join(linhas))    
saida.write('\n);\n')
saida.write('?>')

