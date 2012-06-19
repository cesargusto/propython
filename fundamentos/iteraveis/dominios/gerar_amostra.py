import sys
import io
import itertools
import random

def cinco_pct():
    return randrange(100) < 5

with io.open(sys.argv[1], encoding='utf-8') as arq_entrada:
    with io.open(sys.argv[2], 'wt', encoding='utf-8') as arq_saida:
        for lin in itertools.ifilter(cinco_pct, arq_entrada):
            arq_saida.write(lin)
