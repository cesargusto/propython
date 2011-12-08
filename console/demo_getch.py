#!/usr/bin/env python

from getch import getch
from sys import stdout
from time import strftime

def ctrl(char):
    return chr(ord(char.upper())-ord('A')+1)

CR = chr(13)
hora = ''
print "Tecle CTRL+Q para sair"
while True:
    c = getch()
    if c == ctrl('Q'):
        break
    elif c == CR:
        stdout.write(CR+'\n')
    elif ord(c) < 32:
        stdout.write(repr(c)[1:-1])
    else:
        stdout.write(c)
print
    