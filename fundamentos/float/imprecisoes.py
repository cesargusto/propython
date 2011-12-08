MAX = 1000
sem_erro = 0
for i in range(MAX):
    for j in range(MAX):
        nsoma = i + float(j)/MAX
        nrepr = repr(nsoma)
        nstr = str(nsoma)
        #print nstr, nrepr
        if nstr == nrepr:
            sem_erro += 1
print MAX*MAX, 'valores'
pct = float(sem_erro) / (MAX*MAX) * 100
print '%s sem erro (%0.2f %%)' % (sem_erro, pct)            

