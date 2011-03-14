#!/usr/bin/env python
# coding: utf-8

from Tkinter import *

class Janela(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        bt_sair = Button(self)
        bt_sair['text'] = 'Clique-me'
        bt_sair['font'] = 'Helvetica 48 bold'
        bt_sair['command'] = self.quit
        bt_sair.pack()
 
raiz = Tk()
j = Janela(raiz)
j.mainloop()
raiz.destroy()
 

