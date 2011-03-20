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
        self.current_x = CANVAS_SIZE/2
        self.current_y = CANVAS_SIZE/2
        self.bt1_down = False

    def atualiza(self, joystick, mask):
        char = joystick.read(1)
        self.stick_evt += char
        if len(self.stick_evt) == 8:
            timestamp, position, group, control = struct.unpack('ihBB',self.stick_evt)
            if group == 1:
                descr = 'button %s %s' % (control+1,
                                          'press' if position else 'release')
                self.bt1_down = bool(position)
            elif group == 2:
                axis = 'XYZ'[control]
                descr = '%s axis %d' % (axis, position)
                if axis == 'X':
                    x = self.stick2canvas(position)
                    self.canvas.coords(self.x_line, x, 0, x, CANVAS_SIZE)
                    self.current_x = x
                elif axis == 'Y':
                    y = self.stick2canvas(position)
                    self.canvas.coords(self.y_line, 0, y, CANVAS_SIZE, y)
                    self.current_y = y
            elif group == 0x81:
                descr = 'button %s present' % (control+1)
            elif group == 0x82:
                descr = 'axis %s present; position %d' % ('XYZ'[control], position)
            else:
                descr = '?'
            if self.bt1_down:
                self.canvas.create_oval(self.current_x-MARK_SIZE/2,
                                             self.current_y-MARK_SIZE/2,
                                             self.current_x+MARK_SIZE/2,
                                             self.current_y+MARK_SIZE/2,
                                             fill="blue")
            self.label['text'] = descr
            self.stick_evt = ''

    def stick2canvas(self, n):
        return (n+float(JOYSTICK_RANGE)/2)/JOYSTICK_RANGE*int(self.canvas['width'])

raiz = Tk()
joystick = open('/dev/input/js0','r')
j = Janela(raiz)
# a proxima linha faz disparar o método j.atualiza sempre
# que o joystick # tem dados prontos para leitura
# que o joystick # tem dados prontos para leitura
raiz.createfilehandler(joystick, tkinter.READABLE, j.atualiza)
j.mainloop()
