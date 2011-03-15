#!/usr/bin/env python
# coding: utf-8

from Tkinter import *

class Janela(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.bt = Button(self)
        self.bt['text'] = 'Clique-me'
        self.bt['font'] = 'Helvetica 48 bold'
        self.bt['command'] = self.quit
        self.bt.pack()

raiz = Tk()      # a janela raiz é construída
j = Janela(raiz) # o nosso frame é constuída sobre a janela raiz
j.mainloop()     # o laço de eventos é iniciado
raiz.destroy()   # o laço de eventos não está mais rodando, mas a janela continua
