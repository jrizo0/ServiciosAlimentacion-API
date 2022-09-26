from rest_framework.views import APIView
from .models import Tarifav, Tarifa
from .serializers import TarifavSerializer, TarifaSerializer

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework import generics


class RestauranteViewSet(ModelViewSet):
    serializer_class = TarifavSerializer
    queryset = Tarifav.objects.all()
    lookup_field = "idtarifav"
    http_method_names = ["get", "post", "put", "delete"]

    def dispatch(self, *args, **kwargs):
        return super(RestauranteViewSet, self).dispatch(*args, **kwargs)


# NOTE: ModelViewSet no permite dos pk
class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class RetrieveUpdateDestroyTarifa(
    MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = TarifaSerializer
    queryset = Tarifa.objects.all()
    lookup_fields = ["idtarifav", "codarticulo"]


class ListCreateTarifa(MultipleFieldLookupMixin, generics.ListCreateAPIView):
    serializer_class = TarifaSerializer
    queryset = Tarifa.objects.all()
    lookup_fields = ["idtarifav", "codarticulo"]


class ListTarifaByRestaurante(APIView):
    def get(self, request, idtarifav):
        data = Tarifa.objects.filter(idtarifav=idtarifav)
        serializer = TarifaSerializer(data, many=True)
        res_by_id = {tarifa["codarticulo"]: tarifa for tarifa in serializer.data}
        return Response(res_by_id)
