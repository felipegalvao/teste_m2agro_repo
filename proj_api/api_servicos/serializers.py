from rest_framework import serializers
from .models import Servico, LinhaServico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ('linhas_servico', 'data_inicio', 'data_fim', 'safra', 'custo_total')
        read_only_fields = ['custo_total']
        depth = 1

class LinhaServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinhaServico
        fields = '__all__'
        