from django.db import models

from api_produtos_safra import models as produto_safra_models

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    safra = models.ForeignKey(produto_safra_models.Safra)
    custo_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome 

class LinhaServico(models.Model):
    servico = models.ForeignKey(Servico, related_name="linhas_servico")
    produto = models.ForeignKey(produto_safra_models.Produto, related_name="produtos")
    quantidade = models.IntegerField()
    custo = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.servico.nome + " - " + self.produto.nome

    def save(self, *args, **kwargs):        
        servico = Servico.objects.get(id=self.servico.id)
        servico.custo_total += self.quantidade * self.custo
        servico.save()
        super(LinhaServico, self).save(*args, **kwargs)
         # Call the real save() method
