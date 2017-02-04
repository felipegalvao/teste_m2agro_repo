from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    safra = models.ForeignKey(Safra)
    custo_total = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return 

    def __unicode__(self):
        return 

class LinhaServico(models.Model):
    servico = models.ForeignKey(Servico)
    produto = models.ForeignKey(Produto)
    quantidade = models.IntegerField()
    custo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return 

    def __unicode__(self):
        return 
