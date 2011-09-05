from random import choice

val_linhas = {'0110':6, '1001':9, '1011':9, '1101':9}

str_linhas = {6:'--- x ---',
              7:'---------',
              8:'---   ---',
              9:'----o----'}

def valor(moedas):
    if moedas in val_linhas:
        return val_linhas[moedas]
    else:
        return 8 if moedas[-1] == '0' else 7

def sorteio():
    return ''.join(choice('01') for i in range(4))

linhas = [sorteio() for i in range(6)]

for i, linha in enumerate(reversed(linhas)):
    print 6-i, linha, valor(linha), str_linhas[valor(linha)]

