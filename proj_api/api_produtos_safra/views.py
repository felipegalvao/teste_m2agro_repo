from django.shortcuts import render
from django.http import Http404
from django.db.models import Sum
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

import datetime

from api_servicos.models import Servico, LinhaServico
from .models import Produto, Safra
from .serializers import ProdutoSerializer, SafraSerializer

class ProdutoList(generics.ListCreateAPIView):
    """ Lista todos os produtos """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou deleta um produto
    """
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

def ProdutoUpdatePrecoMedio(request):
    today = datetime.date.today()
    first = today.replace(day=1)
    lastDayLastMonth = first - datetime.timedelta(days=1)
    firstDayLastMonth = lastDayLastMonth.replace(day=1)
    produtos = Produto.objects.all()
    for produto in produtos:
        linhas_servico = LinhaServico.objects.filter(produto=produto, 
                                                     servico__data_fim__lte=lastDayLastMonth,
                                                     servico__data_fim__gte=firstDayLastMonth)
        custo_total = 0
        quantidade_total = 0
        for linha in linhas_servico:
            custo_total += linha.custo * linha.quantidade
            quantidade_total += linha.quantidade
        preco_medio = custo_total / quantidade_total
        produto.preco_medio = preco_medio
        produto.save()
    return redirect('/produtos')

class SafraList(generics.ListCreateAPIView):
    """ Lista todas as safras """
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer

class SafraDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou deleta uma safra
    """
    queryset = Safra.objects.all()
    serializer_class = SafraSerializer
