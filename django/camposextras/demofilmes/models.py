# coding: utf-8

from django.db import models
from time import localtime

ANO_ATUAL = localtime()[0]
PAPEIS = 'diretor produtor ator'.split()

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField(default=ANO_ATUAL)
    
    class Meta:
        ordering = ['titulo', 'ano']
    
    def __unicode__(self):
        return u'%s (%s)' % (self.titulo, self.ano)
        
    def creditos(self):
        for papel in PAPEIS:
            for credito in self.credito_set.filter(papel=papel):
                yield dict(papel=credito.papel, nome=credito.nome)
        
    @models.permalink
    def get_absolute_url(self):
        return ('demofilmes.ver', [str(self.id)])
    
class Credito(models.Model):
    filme = models.ForeignKey(Filme)
    nome = models.CharField(max_length=255)
    papel = models.CharField(max_length=32, choices=[(i,i) for i in PAPEIS])

    class Meta:
        order_with_respect_to = 'filme'

    def __unicode__(self):
        return u'%s (%s, %s)' % (self.nome, self.papel, self.filme.titulo)

