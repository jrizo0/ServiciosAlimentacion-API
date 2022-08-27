from django.urls import path, include

from rest_framework import routers

from clientes.views import ClienteViewSet, TipoclienteViewSet
from restaurantes.views import RestauranteViewSet
from productos.views import ProductoViewSet, DeptoViewSet, SeccionViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'tipoclientes', TipoclienteViewSet)

router.register(r'productos', ProductoViewSet)
router.register(r'depto', DeptoViewSet)
router.register(r'seccion', SeccionViewSet)

router.register(r'restaurantes', RestauranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tarifas/', include('restaurantes.urls')),
]
