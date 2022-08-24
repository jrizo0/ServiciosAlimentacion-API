from .models import Depto, Seccion, Producto
from .serializers import ProductoSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie

class ProductoViewSet(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    lookup_field = "codarticulo"
    http_method_names = ['get', 'post', 'put', 'delete']

    # @method_decorator(vary_on_cookie)
    # @method_decorator(cache_page(60*1))
    def dispatch(self, *args, **kwargs):
        return super(ProductoViewSet, self).dispatch(*args, **kwargs)
