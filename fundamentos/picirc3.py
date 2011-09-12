#!/usr/bin/env python

from __future__ import print_function # python2.6 compatibility
try: # python2.6 compatibility
    range = xrange
except NameError:
    pass

import sys
from random import uniform

TOTAL_DEFAULT = 10**6

total = int(sys.argv[1]) if len(sys.argv) == 2 else TOTAL_DEFAULT

dentro = 0
for i in range(total):
    p = complex(uniform(-1, 1), uniform(-1, 1))
    if abs(p) <= 1:
        dentro += 1

print('total:', total)
print('dentro:', dentro)
print('pi:', float(dentro)/total*4)
