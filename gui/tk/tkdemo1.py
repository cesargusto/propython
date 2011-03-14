#!/usr/bin/env python
# coding: utf-8

import Tkinter
import time

relogio = Tkinter.Label()
relogio['font'] = 'Helvetica 96 bold'
relogio.pack()

def tictac():
    agora = time.strftime('%H:%M:%S')
    if agora != relogio['text']:
        relogio['text'] = agora
    relogio.after(200, tictac)

tictac()
relogio.mainloop()

