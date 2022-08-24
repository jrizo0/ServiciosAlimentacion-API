from rest_framework import serializers
from .models import Cliente, Tipocliente

class ClienteSerializer(serializers.ModelSerializer):
    # tipo = serializers.SlugRelatedField(
    #     many=False,
    #     read_only=True,
    #     slug_field='descripcion'
    # )

    class Meta:
        model = Cliente
        fields = '__all__'
        # fields = ('codcliente', 'nombrecliente', 'direccion1', 'e_mail', 'tipo')

