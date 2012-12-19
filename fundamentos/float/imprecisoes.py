# coding: utf-8
'''
Demonstração de inconsistências na representação de floats geradas
pelas funções `str` e `repr`
'''

MAX = 1000
sem_erro = 0
for i in range(MAX):
    for j in range(MAX):
        nsoma = i + float(j)/MAX
        nrepr = repr(nsoma)
        nstr = str(nsoma)
        if nstr == nrepr:
            sem_erro += 1
        else:
            print nstr, nrepr
print MAX*MAX, 'valores'
pct = float(sem_erro) / (MAX*MAX) * 100
print '%s sem erro (%0.2f %%)' % (sem_erro, pct)

