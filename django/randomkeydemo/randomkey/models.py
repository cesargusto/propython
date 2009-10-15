from django.db import models

from datetime import datetime

class Reserva(models.Model):
    nome = models.CharField(max_length=256)
    data_viagem = models.DateTimeField()
    data_reserva = models.DateTimeField(default=datetime.now, editable=False)
    localizador = models.CharField(max_length=32, editable=False, blank=True)
    
    def save(self):
        
