#!/usr/bin/env python
# coding: utf-8 
total = 0
while True:
    parcela = input('+ ')
    if len(parcela) == 0: 
        break
    try:
        total += float(parcela)
    except ValueError:
        print('???')
        continue  
print('-' * 20)
print(total)
