#!/usr/bin/env python
# coding: utf-8

'''
http://effbot.org/tkinterbook/canvas.htm
'''

import sys
import time

import Tkinter as tk

FATOR = 2
LARG_TOTAL = 574*FATOR
ALT_TOTAL = 250*FATOR
LARG_MODULO = 8*FATOR
ALT_MODULO = 50*FATOR

print 'iniciando', time.strftime('%H:%M:%S')

class Janela(tk.Tk):
    def __init__(self, raiz):
        tk.Tk.__init__(self, raiz)
        self.canvas = tk.Canvas(raiz, width=LARG_TOTAL, height=ALT_TOTAL, bg='#FFFF00')
        self.canvas.pack()
        self.canvas.bind('<Double-Button-1>', lambda e: sys.exit())
        #self.bind_all('<Left>', lambda e: self.desenhar_tabela(-1))
        #self.bind_all('<Right>', lambda e: self.desenhar_tabela(1))
        self.geometry('+1800+300')
        self.desenhar_base()

    def desenhar_base(self):
        c = self.canvas
        x0 = y0 = 10
        c.create_rectangle(x0, y0, x0+LARG_MODULO, y0+ALT_MODULO, fill='white')
        #c.create_circle()
                            



janela = Janela(None)
janela.mainloop()
