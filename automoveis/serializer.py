from rest_framework import serializers
from automoveis.models import Carro, Moto, Caminhao


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'

class CaminhaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caminhao
        fields = '__all__'