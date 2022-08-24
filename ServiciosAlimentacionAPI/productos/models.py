from django.db import models

class Depto(models.Model):
    numdpto = models.SmallIntegerField(db_column='NUMDPTO', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=50, db_collation='Latin1_General_100_CS_AI_SC_UTF8')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPTO'

class Seccion(models.Model):
    numdpto = models.ForeignKey(Depto, models.DO_NOTHING, db_column='NUMDPTO')  # Field name made lowercase.
    numseccion = models.SmallIntegerField(db_column='NUMSECCION', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=50, db_collation='Latin1_General_100_CS_AI_SC_UTF8')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SECCION'


class Producto(models.Model):
    codarticulo = models.SmallIntegerField(db_column='CODARTICULO', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='DESCRIPCION', max_length=50, db_collation='Latin1_General_100_CS_AI_SC_UTF8')  # Field name made lowercase.
    dpto = models.ForeignKey(Depto, models.DO_NOTHING, db_column='DPTO')  # Field name made lowercase.
    seccion = models.ForeignKey('Seccion', models.DO_NOTHING, db_column='SECCION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCTO'
