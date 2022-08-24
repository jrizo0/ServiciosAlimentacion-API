from .models import Tarifav, Tarifa
from .serializers import TarifavSerializer, TarifaSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie

#Tarifav === Restaurante

class RestauranteViewSet(ModelViewSet):
    serializer_class = TarifavSerializer
    queryset = Tarifav.objects.all()
    lookup_field = "idtarifav"
    http_method_names = ['get', 'post', 'put', 'delete']

    # @method_decorator(vary_on_cookie)
    # @method_decorator(cache_page(60*1))
    def dispatch(self, *args, **kwargs):
        return super(RestauranteViewSet, self).dispatch(*args, **kwargs)
