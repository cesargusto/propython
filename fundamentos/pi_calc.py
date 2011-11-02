# source: http://rosettacode.org/wiki/Pi

import sys

def calc_pi(width=70):
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    digits = ''
    while True:
        if 4*q+r-t < n*t:
            digits += str(n)
            if len(digits) == width:
                yield digits
                digits = ''
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr

try:
    width = int(sys.argv[1])
except (IndexError, ValueError):
    width = 70
 
for lin in calc_pi(width):
    print(lin)