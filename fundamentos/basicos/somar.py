#!/usr/bin/env python
# coding: utf-8 

total = 0
while True:
    parcela = raw_input('+ ')
    if len(parcela) == 0: 
        break
    try:
        total += float(parcela)
    except ValueError:
        print '???'  
print '-' * 20
print total
