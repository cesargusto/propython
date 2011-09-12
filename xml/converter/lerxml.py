# coding: utf-8

from xml.etree import ElementTree

mapa = ElementTree.parse('crtp-freemind.mm')

raiz = mapa.getroot()

node0 = raiz.getchildren()[0]

def descascar(elemento, nivel, acao, *args):
    acao(elemento, nivel, *args)
    for sub in elemento.getchildren():
        descascar(sub, nivel+1, acao, *args)    

def minha_acao(elemento, nivel):
    indent = '  '*nivel
    print '%s%s' % (indent, elemento.get('TEXT'))    

def outra_acao(elemento, nivel):
    indent = '*'*nivel
    print '%s%s' % (indent, elemento.get('TEXT'))    

def gravar_linha(elemento, nivel, arq):
    indent = '  '*nivel
    arq.write('%s%s\n' % (indent, elemento.get('TEXT')))

arq = open('saida.txt', 'w')
descascar(node0, 0, gravar_linha, arq)
arq.close()




