# coding: utf-8
'''
http://effbot.org/tkinterbook/canvas.htm
''' 

import sys
from Tkinter import *

CEL = 44
LATERAL = CEL * 6

ESTILO_ROTULO = dict(anchor='center', font='courier 24', fill='gray')
ESTILO_CAR = dict(anchor='center', font='times 32', fill='black')        
ESTILO_LEGENDA = dict(anchor='w', font='helvetica 32', fill='black')

CODEPAGES = ['ASCII', 'cp437', 'cp850', 
'ISO-8859-1', 'ISO-8859-2', 'ISO-8859-3', 'ISO-8859-4', 'ISO-8859-5', 'KOI8-R', 
'ISO-8859-6', 'ISO-8859-7', 'ISO-8859-8', 'ISO-8859-9', 
# 'ISO-8859-10', 'ISO-8859-6-E', 'ISO-8859-6-I', 'ISO-8859-8-E', 'ISO-8859-8-I',
# 'ISO-8859-14', 'ISO-8859-16', 'Shift_JIS', 'Windows-31J'
'ISO-8859-13', 'ISO-8859-15', 
'Windows-1252', 'Windows-1251', 'MacRoman']     

class Janela(Frame):
    def __init__(self, raiz):
        Frame.__init__(self, raiz)
        self.canvas = Canvas(raiz, width=CEL*17+LATERAL, height=CEL*17)
        self.cels = [[0]*16 for i in range(16)]
        self.canvas.pack()
        self.desenhar_base()
        self.canvas.bind('<Double-Button-1>', lambda e: sys.exit())
        self.bind_all('<Left>', lambda e: self.desenhar_tabela(-1))
        self.bind_all('<Right>', lambda e: self.desenhar_tabela(1))
        self.id_pg = 0 # ASCII
        raiz.geometry('+1800+300')

    def mudar_legenda(self, texto):
        if hasattr(self, 'legenda'):
            self.canvas.delete(self.legenda)
        self.legenda = self.canvas.create_text(17.5*CEL, 1.5*CEL, text=texto, **ESTILO_LEGENDA)

    def desenhar_tabela(self, muda_cod):
        self.id_pg_anterior = self.id_pg
        self.id_pg += muda_cod
        if self.id_pg < 0:
            self.id_pg = len(CODEPAGES)-1
        elif self.id_pg == len(CODEPAGES):
            self.id_pg = 0
        encoding = CODEPAGES[self.id_pg]
        self.mudar_legenda(encoding)
        self.canvas.delete('page%d' % self.id_pg_anterior)
        if self.id_pg > 0: # alem do ASCII
            for i in range(8, 16):
                for j in range(16):
                    car = chr(i*16+j).decode(encoding, 'ignore')
                    self.cels[i][j] = self.canvas.create_text((j+1.5)*CEL, (i+1.5)*CEL, 
                        text=car, tag='page%d' % self.id_pg, **ESTILO_CAR)


    def desenhar_base(self):
        c = self.canvas
        self.mudar_legenda('ASCII')
        for i in range(17):
            # linhas
            c.create_line(CEL, (i+1)*CEL, 17*CEL, (i+1)*CEL)
            c.create_line((i+1)*CEL, CEL, (i+1)*CEL, 17*CEL)
            if i < 16:
                # rótulo
                c.create_text((i+1.6)*CEL, CEL/2, text=u'_%X'%i, **ESTILO_ROTULO)
                c.create_text(CEL/2, (i+1.5)*CEL, text=u'%X0'%i, **ESTILO_ROTULO)
                for j in range(16):
                    # tabela ASCII
                    code = i*16 + j
                    if 32 <= code < 128:
                        self.cels[i][j] = c.create_text((j+1.5)*CEL, (i+1.5)*CEL, text=unichr(code), **ESTILO_CAR)
                    elif code == 128:
                        break
                    



raiz = Tk()
Janela(Tk()).mainloop()
