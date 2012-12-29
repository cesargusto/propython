from random import choice, randrange

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

def reproduzir(pais):
    corte = randrange(1, TAM_SENHA-1)
    geracao = pais + [pais[0][:corte]+pais[1][corte:],
                      pais[1][:corte]+pais[0][corte:]]
    # mutacao
    if randrange(100) == 1:
        filho = randrange(2, 4)
        posicao = randrange(TAM_SENHA)
        mutante = list(geracao[filho])
        mutante[posicao] = choice(SIMBOLOS)
        geracao[filho] = ''.join(mutante)
    return geracao


meta = gerar()

print meta
eleitos = [gerar(), gerar()]
geracao = reproduzir(eleitos)

tentativas = 1
while True:
    avaliacoes = []
    for exemplar in geracao:
        avaliacoes.append( (avaliar(meta, exemplar), exemplar) )
    avaliacoes.sort(key=lambda aval:aval[0], reverse=True)
    eleitos = [avaliacoes[0][1], avaliacoes[1][1]]
    if eleitos[0] == meta:
        break
    geracao = reproduzir(eleitos)
    print tentativas, geracao
    tentativas += 1
print eleitos[0]




