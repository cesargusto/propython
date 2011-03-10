#!/usr/bin/env python

import sys
from random import uniform

TOTAL_DEFAULT = 10**6

total = int(sys.argv[1]) if len(sys.argv) == 2 else TOTAL_DEFAULT

dentro = 0
for i in xrange(total):
    p = complex(uniform(-1, 1), uniform(-1, 1))
    if abs(p) <= 1:
        dentro += 1

print 'total:', total
print 'dentro:', dentro
print 'pi:', float(dentro)/total*4
