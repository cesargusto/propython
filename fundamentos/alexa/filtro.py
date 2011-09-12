#!/usr/bin/env python

interessantes = '''sld.cu saude salud bireme'''.split()

for lin in file('top-100k.csv'):
    for p in interessantes:
        if p in lin:
            print lin.strip().replace(',','\t')
