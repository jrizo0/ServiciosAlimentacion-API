from rest_framework import serializers
from .models import Cliente, Tipocliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CreateClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["nombrecliente", "direccion1", "e_mail", "tipo"]

class TipoclienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipocliente
        fields = '__all__'
