from rest_framework import serializers
from .models import Produto, Safra

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        read_only_fields = ['custo_medio']

class SafraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safra
        fields = '__all__'
    