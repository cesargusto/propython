# coding: utf-8
'''
http://effbot.org/tkinterbook/canvas.htm
''' 

import sys
from Tkinter import Tk, Frame, Canvas
import math

CEL = 44
LATERAL = CEL * 6
DIST_APROX = 2 # distancia considerada suficientemente proxima para ser igual

ESTILO_ROTULO = dict(anchor='center', font='courier 24', fill='gray')
ESTILO_CAR = dict(anchor='center', font='times 32', fill='black')        
ESTILO_LEGENDA = dict(anchor='w', font='helvetica 32', fill='black')

CODEPAGES = ['ASCII', 'cp437', 'cp850', 'MacRoman', 
'ISO-8859-1', 'ISO-8859-15', 'Windows-1252', 'ISO-8859-13', 'ISO-8859-2', 'ISO-8859-3', 'ISO-8859-9', 'ISO-8859-4', 
'ISO-8859-7', 'ISO-8859-8', 
# 'ISO-8859-10', 'ISO-8859-6-E', 'ISO-8859-6-I', 'ISO-8859-8-E', 'ISO-8859-8-I',
# 'ISO-8859-14', 'ISO-8859-16', 'Shift_JIS', 'Windows-31J'
 
'ISO-8859-5', 'Windows-1251', 'KOI8-R', 'cp437', ]

class Glifo(object):
    ativos = {}
    movendo = {}

    def __init__(self, canvas, unicar, x, y):
        self.canvas = canvas
        self.unicar = unicar
        self.x = x
        self.y = y
        self.vx = self.vy = self.ax = self.ay = 0
        self.x_dest = self.y_dest = None
        Glifo.ativos[self.unicar] = self
        self.handle = self.canvas.create_text(x, y, 
                        text=unicar, **ESTILO_CAR)

    def partir(self, x_dest, y_dest):
        Glifo.movendo[self.unicar] = self
        self.x_dest = x_dest
        self.y_dest = y_dest
        self.direcao = math.atan2(self.y_dest-self.y, self.x_dest-self.x)
        self.vx = math.cos(self.direcao)
        self.vy = math.sin(self.direcao)
        self.ax = self.vx
        self.ay = self.vy
        self.distancia = math.hypot(self.x-self.x_dest, self.y-self.y_dest)

    def mover(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax
        self.vy += self.ay
        distancia = math.hypot(self.x-self.x_dest, self.y-self.y_dest)
        if distancia <= DIST_APROX or distancia > self.distancia: # chegamos ou passamos
            self.parar()
        else:
            self.distancia = distancia
        self.canvas.coords(self.handle, (self.x, self.y))
        #print self.unicar, self.x, self.y, self.vx, self.vy, self.direcao

    def parar(self):
        self.x = self.x_dest
        self.y = self.y_dest
        self.vx = self.vy = self.ax = self.ay = 0
        del Glifo.movendo[self.unicar]

    @classmethod
    def remover(cls, unicar):
        glifo = cls.ativos.pop(unicar)    
        glifo.canvas.delete(glifo.handle)
        if unicar in Glifo.movendo: del Glifo.movendo[unicar]    

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
        unicars_sobrando = set(Glifo.ativos)
        if self.id_pg > 0: # alem do ASCII
            for i in range(8, 16):
                for j in range(16):
                    unicar = chr(i*16+j).decode(encoding, 'ignore')
                    if not unicar:
                        continue
                    glifo = Glifo.ativos.get(unicar)
                    if glifo is None:
                        glifo = Glifo(self.canvas, unicar, 17.5*CEL, 1.5*CEL)
                    else:
                        unicars_sobrando.remove(unicar)
                    glifo.partir((j+1.5)*CEL, (i+1.5)*CEL)
        for unicar in unicars_sobrando:
            Glifo.remover(unicar)
        self.atualizar()

    def atualizar(self):
        # print Glifo.movendo.keys()
        if Glifo.movendo:
            for unicar, glifo in Glifo.movendo.items():
                glifo.mover()
            self.after(50, self.atualizar)

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
Janela(raiz).mainloop()
