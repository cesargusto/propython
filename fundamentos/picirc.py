#!/usr/bin/env python

import sys
from random import uniform
from math import sqrt

TOTAL_DEFAULT = 10**6

total = int(sys.argv[1]) if len(sys.argv) == 2 else TOTAL_DEFAULT

dentro = 0
for i in xrange(total):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if sqrt(x*x+y*y) <= 1:
        dentro += 1

print 'total:', total
print 'dentro:', dentro
print 'pi:', float(dentro)/total*4
