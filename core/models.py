from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('Email')
    senha = models.DecimalField('Senha',decimal_places=2,max_digits=8)
