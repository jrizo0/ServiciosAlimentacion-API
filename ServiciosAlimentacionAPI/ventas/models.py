from django.db import models

from productos.models import Producto

class Ventas(models.Model):
    transaccion = models.CharField(db_column='TRANSACCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codarticulo = models.ForeignKey(Producto, models.DO_NOTHING, db_column='CODARTICULO')  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    unidadestotal = models.FloatField(db_column='UNIDADESTOTAL', blank=True, null=True)  # Field name made lowercase.
    precio = models.FloatField(db_column='PRECIO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENTAS'

