from django.urls import path, include

from rest_framework import routers

from .views import ClienteViewSet

app_name = 'clientes'

router = routers.DefaultRouter()

router.register(r'', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
