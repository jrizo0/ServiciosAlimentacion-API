from rest_framework import serializers
from .models import Producto, Depto, Seccion

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DeptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depto
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

