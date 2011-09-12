import sys
from math import sqrt
from random import uniform

TOTAL_DEFAULT = 10**6

if len(sys.argv) == 2:
    total = int(sys.argv[1])
else:
    total = TOTAL_DEFAULT
    
dentro = 0    
for i in xrange(total):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if sqrt((x*x)+(y*y)) <= 1:
        dentro += 1
print 'total:', total
print 'dentro:', dentro
print 'pi:', float(dentro)/total*4
