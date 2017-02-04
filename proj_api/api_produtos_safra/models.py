from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_medio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class Safra(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome
