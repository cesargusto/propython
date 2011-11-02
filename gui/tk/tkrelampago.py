#!/usr/bin/env python
# coding: utf-8

import Tkinter
from time import time
import sys

TEMPO = 10 if len(sys.argv) == 1 else int(sys.argv[1])

def reset():
    global inicio
    inicio = time()

def tictac():
    dt = TEMPO - int(time() - inicio)
    if dt > 0:
        agora = '{m}:{s:02d}'.format(m=dt/60, s=dt%60)
        if agora != relogio['text']:
            relogio['text'] = agora
    else:        
        relogio['text'] = '0:00'
        relogio['fg'] = 'yellow' if relogio['fg'] == 'red'  else 'red'
    relogio.after(200, tictac)

relogio = Tkinter.Button()
relogio['font'] = 'Helvetica 240 bold'
relogio['command'] = reset
relogio.pack()

reset()
tictac()
relogio.mainloop()

