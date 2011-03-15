#!/usr/bin/env python
# coding: utf-8

import pyglet
from pyglet.window import key
from vetor import Vetor as V

pyglet.resource.path = ['imagens']
pyglet.resource.reindex()

LARG_JANELA = 800
ALT_JANELA = 600
ALT_POUSO = 50
GRAVIDADE = V(0,-1)

acoplado = True

class Nave(pyglet.sprite.Sprite):
    def __init__(self, arq_img, x, y, vx=0, vy=0):
        self.figura = pyglet.resource.image(arq_img)
        self.vel = V(vx, vy)
        super(Nave, self).__init__(self.figura, x, y)
        self.parando = False
        
    def acelerar(self, acel):
        self.vel = self.vel + acel

    def update(self, dt):
        self.acelerar(GRAVIDADE)
        self.x = (self.x + self.vel.x) % LARG_JANELA
        self.y += self.vel.y
        if self.y > (ALT_JANELA - self.height):
            self.y = ALT_JANELA - self.height
            self.vel = V(self.vel.x, 0)
        elif self.y < ALT_POUSO:
            self.y = ALT_POUSO
            self.vel = V(0,0)
        
class PousoLunar(pyglet.window.Window):
    def __init__(self):
        super(PousoLunar, self).__init__(LARG_JANELA, ALT_JANELA)
        self.fundo = pyglet.resource.image('earthrise800x600.jpg')
        self.mc = Nave('cm-corgi.png', 100, 500)
        self.lem = Nave('lem.png', self.mc.x-14, self.mc.y-54)

        self.mc.vel = self.lem.vel = V(2, 0)
        
        pyglet.clock.schedule_interval(self.atualizar_sprites, 1/60.)
        pyglet.app.run()
        
    def atualizar_sprites(self, dt):
        self.mc.update(dt)
        self.lem.update(dt)

    def on_draw(self):
        self.clear()
        self.fundo.blit(0, 0)
        self.mc.draw()
        self.lem.draw()
                
    def on_key_press(self, symbol, modifiers):
        global acoplado
        if symbol == key.RIGHT:
            self.lem.acelerar(V(1,0))
        elif symbol == key.LEFT:
            self.lem.acelerar(V(-1,0))
        elif symbol == key.UP:
            self.lem.acelerar(V(0,2))
        elif symbol == key.DOWN:
            self.lem.acelerar(V(0,-1))
        elif symbol == key.P:
            self.lem.parando = True
        elif symbol == key.D and modifiers == 2:
            import pdb; pdb.set_trace()
        elif symbol == key.ESCAPE:
            raise SystemExit

if __name__ == '__main__':
    PousoLunar()
