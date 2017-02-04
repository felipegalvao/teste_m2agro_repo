from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Servico, LinhaServico
from .serializers import ServicoSerializer, LinhaServicoSerializer

class ServicoList(generics.ListCreateAPIView):
    """ Lista todos os Serviços """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou deleta um serviço
    """
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class LinhaServicoList(generics.ListCreateAPIView):
    """ Lista todos as Linhas de Serviço """
    queryset = LinhaServico.objects.all()
    serializer_class = LinhaServicoSerializer

class LinhaServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Recupera, atualiza ou deleta uma linha de serviço
    """
    queryset = LinhaServico.objects.all()
    serializer_class = LinhaServicoSerializer