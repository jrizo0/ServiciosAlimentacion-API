from .models import Cliente, Tipocliente
from .serializers import ClienteSerializer, TipoclienteSerializer

from rest_framework.viewsets import ModelViewSet


class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    lookup_field = "codcliente"
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)

class TipoclienteViewSet(ModelViewSet):
    serializer_class = TipoclienteSerializer
    queryset = Tipocliente.objects.all()
    lookup_field = "idtipo"
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        return super(TipoclienteViewSet, self).dispatch(*args, **kwargs)
