#!/usr/bin/env python
# coding: utf-8

import pyglet
from pyglet.window import key
from vetor import Vetor as V

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

LARG_JANELA = 800
ALT_JANELA = 600

class Nave(pyglet.sprite.Sprite):
    def __init__(self, arq_img, x, y):
        self.figura = pyglet.resource.image(arq_img)
        self.vel = V(0, 0)
        super(Nave, self).__init__(self.figura, x, y)
        
    def acelerar(self, acel):
        self.vel = self.vel + acel

    def update(self, dt):
        self.x = (self.x + self.vel.x) % LARG_JANELA
        self.y += self.vel.y
        if self.y > (ALT_JANELA - self.height):
            self.y = ALT_JANELA - self.height
        
class PousoLunar(pyglet.window.Window):
    def __init__(self):
        super(PousoLunar, self).__init__(LARG_JANELA, ALT_JANELA)
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        self.mc = Nave('cm-corgi.png', 100, 500)

        self.lems = []
        for i in range(6):
            self.lems.append(Nave('lem.png', self.mc.x-15, self.mc.y-56-i*60))
            self.lems[i].vel = V(2, 0)                        
        self.mc.vel = V(2, 0)
        
        pyglet.clock.schedule_interval(self.atualizar_sprites, 1/60.)
        pyglet.app.run()
        
    def atualizar_sprites(self, dt):
        self.mc.update(dt)
        for i in range(6):
            self.lems[i].update(dt)

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)
        self.mc.draw()
        for i in range(6):
            self.lems[i].draw()
                
    def on_key_press(self, symbol, modifiers):
        if symbol == key.RIGHT:
            self.lem.acelerar(V(1,0))
        elif symbol == key.LEFT:
            self.lem.acelerar(V(-1,0))
        elif symbol == key.UP:
            self.lem.acelerar(V(0,1))
        elif symbol == key.DOWN:
            self.lem.acelerar(V(0,-1))

if __name__ == '__main__':
    PousoLunar()
