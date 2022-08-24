from django.urls import path, include

from rest_framework import routers

from clientes.views import ClienteViewSet
from restaurantes.views import RestauranteViewSet
from productos.views import ProductoViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'productos', RestauranteViewSet)
router.register(r'restaurantes', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
