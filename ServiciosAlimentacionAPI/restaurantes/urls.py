from django.urls import path

from .views import RetrieveUpdateDestroyTarifa, ListCreateTarifa, ListTarifaByRestaurante

urlpatterns = [
    path(r'<int:idtarifav>/<int:codarticulo>', RetrieveUpdateDestroyTarifa.as_view()),
    path(r'', ListCreateTarifa.as_view()),
    path(r'<int:idtarifav>/', ListTarifaByRestaurante.as_view()),
]
