from .models import Depto, Seccion, Producto
from .serializers import ProductoSerializer, DeptoSerializer, SeccionSerializer

from rest_framework.viewsets import ModelViewSet

class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    lookup_field = "codarticulo"
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        return super(ProductoViewSet, self).dispatch(*args, **kwargs)

class DeptoViewSet(ModelViewSet):
    serializer_class = DeptoSerializer
    queryset = Depto.objects.all()
    lookup_field = "numdpto"
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        return super(DeptoViewSet, self).dispatch(*args, **kwargs)

class SeccionViewSet(ModelViewSet):
    serializer_class = SeccionSerializer
    queryset = Seccion.objects.all()
    lookup_field = "numseccion"
    http_method_names = ['get', 'post', 'put', 'delete']

    def dispatch(self, *args, **kwargs):
        return super(SeccionViewSet, self).dispatch(*args, **kwargs)
