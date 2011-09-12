#!/usr/bin/env python
# coding: utf-8

entrada = raw_input('Por favor digite a letra e minúscula com acento agudo (é): ')
if entrada == '\xc3\xa9':
    print 'Este console é UTF-8'
elif entrada == '\xe9':
    print 'Este console é CP1252, ISO-8859-1 ou compatível'
    
