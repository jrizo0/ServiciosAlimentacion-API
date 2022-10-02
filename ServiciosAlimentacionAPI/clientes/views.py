from .models import Cliente, Tipocliente
from .serializers import (
    ClienteSerializer,
    TipoclienteSerializer,
    CreateClienteSerializer,
)

from rest_framework.serializers import ValidationError
from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response


class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    lookup_field = "codcliente"
    http_method_names = ["get", "post", "put", "delete"]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateClienteSerializer
        return ClienteSerializer

    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        if Cliente.objects.filter(e_mail=request.data["e_mail"]).exists():
            raise ValidationError("Email ya existe")
        serializer_create = CreateClienteSerializer(data=request.data)
        serializer_create.is_valid(raise_exception=True)

        new_cliente_obj = serializer_create.save()
        serializer = ClienteSerializer(new_cliente_obj)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class TipoclienteViewSet(ModelViewSet):
    serializer_class = TipoclienteSerializer
    queryset = Tipocliente.objects.all()
    lookup_field = "idtipo"
    http_method_names = ["get", "post", "put", "delete"]

    def dispatch(self, *args, **kwargs):
        return super(TipoclienteViewSet, self).dispatch(*args, **kwargs)
