#!/usr/bin/env python
# coding: utf-8

import re
from urllib import urlopen
from random import shuffle

URL = 'https://garoa.net.br/w/index.php?title=Associados&action=edit'

INICIO = '==Associados Efetivos=='
FIM = '</div>'
RE_NOME = r'\* \[\[Usuário:[^|]+\|([^\]]+)'
RE_NOME = re.compile(RE_NOME)

lendo = False

associados = []
for lin in urlopen(URL):
    lin = lin.strip()
    if lin == INICIO:
        lendo = True
        continue
    elif lendo and lin == FIM:
        break
    if lendo:
        if not lin.startswith('* '):
            continue
        bateu = RE_NOME.match(lin)
        nome = bateu.group(1) if bateu else lin[2:]
        associados.append(nome)

shuffle(associados)
grupos = []
grupos.append(sorted(associados[:len(associados)/2]))
grupos.append(sorted(associados[len(associados)/2:]))

for n, grupo in enumerate(grupos):
    print '=== Grupo', n, '==='
    for nome in grupo:
        print '\t'+nome
    print
    
    


