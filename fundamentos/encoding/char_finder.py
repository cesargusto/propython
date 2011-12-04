#!/usr/bin/env python
from unicodedata import name
import sys

if len(sys.argv) > 1:
    words = sys.argv[1:]
else:
    words = raw_input('search words: ').split()

words = [s.lower() for s in words]

count = 0
for i in range(20, sys.maxunicode):
    car = unichr(i)
    descr = name(car, 'no-name')
    if descr == 'no-name':
        continue
    low_descr = descr.lower()
    if all(word in low_descr for word in words):
        print u'{i:5d} {i:04x} {car:^5} {descr}'.format(**locals())
        count += 1

print '{0} character(s) found'.format(count)
