from django.urls import path

from .views import RetrieveUpdateDestroyTarifa, ListCreateTarifa, ListTarifaByRestaurante

urlpatterns = [
    path('', ListCreateTarifa.as_view()),
    path('<int:idtarifav>/<int:codarticulo>/', RetrieveUpdateDestroyTarifa.as_view()),
    path('tarifav/<int:idtarifav>/', ListTarifaByRestaurante.as_view()),
]
