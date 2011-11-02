#!/usr/bin/env python

from unicodedata import name, category

total = 0x110000

def named(uchar):
    try:
        uname = name(uchar)
        return True
    except ValueError:
        return False

named_ranges = 0
pages = 0
for i in range(0, total, 0x100):
    first_name = ''
    if any( named(unichr(i+j)) for j in range(0x100) ):
        named_ranges += 1
        for k in range(0x100):
            uc = unichr(i+k)
            if named(uc):
                first_name = name(uc)
                cat = category(uc)
                break
        if first_name.startswith('CJK UNIFIED IDEOGRAPH'): continue
        print '%3d %04x %s %s' % (pages, i, cat, first_name)
        pages += 1    

print '%.1f%% named' % (named_ranges/(float(total)/0x100) * 100)
