#!/usr/bin/env python

txt = open('medals-2012-0.txt')

rank = 0
name = ''
medals = []

for i, lin in enumerate(txt):
    if i % 3 == 0:
        rank = int(lin)
    elif i % 3 == 1:
        name = lin.strip()
        name = name[:len(name)/2]
    else:
        medals = [int(x) for x in lin.split()]
        assert len(medals) == 4
        assert sum(medals[:3]) == medals[-1]
        print '%s\t%s\t%s\t%s\t%s\t%s' % tuple([rank, name] + medals)
