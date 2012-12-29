from random import choice

TAM_SENHA = 5
SIMBOLOS = '0123456789'

def gerar():
    res = ''
    for i in range(TAM_SENHA):
        res += choice(SIMBOLOS)
    return res

def avaliar(meta, chute):
    res = 0
    for a, b in zip(meta, chute):
        if a == b:
            res += 1
    return res

meta = gerar()
chute = gerar()

tentativas = 1
while meta != chute:
    print tentativas, 'tentando:', meta, 'chute:', chute
    chute = gerar()
    tentativas += 1

print tentativas, 'tentando:', meta, 'chute:', chute


