from rest_framework import serializers
from .models import Servico, LinhaServico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ('id', 'nome', 'linhas_servico', 'data_inicio', 'data_fim', 'safra', 'custo_total')
        read_only_fields = ['custo_total', 'linhas_servico']

class LinhaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinhaServico
        fields = '__all__'
        