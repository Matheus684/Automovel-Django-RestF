from rest_framework import viewsets, generics, filters
from automoveis.models import Carro, Moto, Caminhao
from automoveis.serializer import CarroSerializer, MotoSerializer, CaminhaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ano_fabricacao', 'preco']
    search_fields = ['marca', 'modelo']

class MotoViewSet(viewsets.ModelViewSet):
    queryset = Moto.objects.all()
    serializer_class = MotoSerializer
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ano_fabricacao', 'preco']
    search_fields = ['marca', 'modelo']

class CaminhaoViewSet(viewsets.ModelViewSet):
    queryset = Caminhao.objects.all()
    serializer_class = CaminhaoSerializer
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ano_fabricacao', 'preco']
    search_fields = ['marca', 'modelo']