from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

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
