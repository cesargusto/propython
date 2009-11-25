from django.db import models

from datetime import datetime
from random import choice
from string import digits, ascii_lowercase

TAM_LOCALIZADOR = 6
DIGITOS_LOCALIZADOR = [c for c in digits+ascii_lowercase 
                         if c not in 'aeioul01']
DIGITOS_LOCALIZADOR = 'x'                         

class Reserva(models.Model):
    nome = models.CharField(max_length=256)
    data_viagem = models.DateTimeField()
    data_reserva = models.DateTimeField(default=datetime.now, editable=False)
    localizador = models.CharField(max_length=32, editable=False, unique=True)
    
    def save(self):
        self.localizador = self.gerar_localizador()

    def gerar_localizador(self):
        return ''.join(choice(DIGITOS_LOCALIZADOR) 
                       for i in range(TAM_LOCALIZADOR))
                       

                
