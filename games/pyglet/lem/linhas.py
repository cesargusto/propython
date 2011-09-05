#!/usr/bin/env python
# coding: utf-8

import pyglet
from pyglet.window import key
from array import array

LARG_JANELA = 800
ALT_JANELA = 600
        
class JaneLinhas(pyglet.window.Window):
    def __init__(self):
        self.clicks = array('i')
        super(JaneLinhas, self).__init__(LARG_JANELA, ALT_JANELA)
        pyglet.app.run()
        
    def on_draw(self):
        self.clear()
        qt_pontos = len(self.clicks) // 2
        if qt_pontos:
            pyglet.graphics.draw(qt_pontos, pyglet.gl.GL_TRIANGLE_FAN,
                                 ('v2i', self.clicks))
            print self.clicks
        
    def on_mouse_press(self, x, y, button, modifiers):
        self.clicks.extend((x,y))
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.D and modifiers == 2:
            import pdb; pdb.set_trace()
        elif symbol == key.ESCAPE:
            raise SystemExit

if __name__ == '__main__':
    JaneLinhas()
