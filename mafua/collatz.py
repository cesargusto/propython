
MAX = 100000

max_passos = 0
n_max_passos = 0

def collatz(n):
    if n % 2:
        return n*3+1
    else:
        return n/2

for i in range(1,MAX+1):
    passos = 0
    n = i
    pico = 0
    #print n,
    while True:
        n = collatz(n)
        if n > pico: pico = n
        #print n,
        passos += 1
        if n == 1:
            break
    #print '(%s passos)' % passos
    if passos > max_passos:
        max_passos = passos
        n_max_passos = i
        print 'n = %4d, passos = %4d, pico = %4d' % (n_max_passos, max_passos, pico)
        
