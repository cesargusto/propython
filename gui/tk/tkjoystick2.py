#!/usr/bin/env python
# coding: utf-8

from Tkinter import *
import os
import struct

CANVAS_SIZE = 640
JOYSTICK_RANGE = 2**16
MARK_SIZE = 10

class Janela(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        self.canvas = Canvas(self, width=CANVAS_SIZE, height=CANVAS_SIZE)
        self.canvas.pack()
        self.label = Label(self, text='evento...')
        self.label.pack()
        self.stick_evt = ''
        self.x_line = self.canvas.create_line(CANVAS_SIZE/2,0,
                                              CANVAS_SIZE/2,CANVAS_SIZE,
                                              fill="red")
        self.y_line = self.canvas.create_line(0, CANVAS_SIZE/2,
                                              CANVAS_SIZE, CANVAS_SIZE/2,
                                              fill="red")
        self.previous_x = CANVAS_SIZE/2
        self.previous_y = CANVAS_SIZE/2
        self.bt1_down = False
        self.bolinhas = []
        self.after(50, self.gravidade)

    def gravidade(self):
        for l in self.bolinhas:
            b, x, y = l
            y2 = y + 2
            self.canvas.coords(b, x-MARK_SIZE/2,
                                  y2-MARK_SIZE/2,
                                  x+MARK_SIZE/2,
                                  y2+MARK_SIZE/2)
            l[2] = y2
        self.after(50, self.gravidade)

    def atualiza(self, joystick, mask):
        char = joystick.read(1) # Python3: UnicodeDecodeError
        self.stick_evt += char
        if len(self.stick_evt) == 8:
            timestamp, position, group, control = struct.unpack('ihBB',self.stick_evt)
            if group == 1:
                descr = 'button %s %s' % (control+1,
                                          'press' if position else 'release')
                self.bt1_down = bool(position)
                if self.bt1_down:
                    self.bolinhas.append([self.canvas.create_oval(self.previous_x-MARK_SIZE/2,
                                                 self.previous_y-MARK_SIZE/2,
                                                 self.previous_x+MARK_SIZE/2,
                                                 self.previous_y+MARK_SIZE/2,
                                                 fill="green"),
                                                 self.previous_x,
                                                 self.previous_y])
            elif group == 2:
                axis = 'XYZ'[control]
                descr = '%s axis %d' % (axis, position)
                x = self.previous_x
                y = self.previous_y
                if axis == 'X':
                    x = self.stick2canvas(position)
                    self.canvas.coords(self.x_line, x, 0, x, CANVAS_SIZE)
                elif axis == 'Y':
                    y = self.stick2canvas(position)
                    self.canvas.coords(self.y_line, 0, y, CANVAS_SIZE, y)
                if self.previous_x != x or self.previous_y != y:
                    self.canvas.create_line(
                                        self.previous_x, self.previous_y,
                                        x, y, fill="blue")

                self.previous_x = x
                self.previous_y = y
            elif group == 0x81:
                descr = 'button %s present' % (control+1)
            elif group == 0x82:
                descr = 'axis %s present; position %d' % ('XYZ'[control], position)
            else:
                descr = '?'
            self.label['text'] = descr
            self.stick_evt = ''

    def stick2canvas(self, n):
        return (n+float(JOYSTICK_RANGE)/2)/JOYSTICK_RANGE*int(self.canvas['width'])

raiz = Tk()
joystick = open('/dev/input/js0','r')
j = Janela(raiz)

# a proxima linha faz disparar o método j.atualiza sempre
# que o joystick # tem dados prontos para leitura
raiz.createfilehandler(joystick, READABLE, j.atualiza)
j.mainloop()
