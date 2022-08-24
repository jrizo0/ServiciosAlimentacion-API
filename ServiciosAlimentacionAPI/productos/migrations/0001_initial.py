# Generated by Django 4.1 on 2022-08-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Depto",
            fields=[
                (
                    "numdpto",
                    models.SmallIntegerField(
                        db_column="NUMDPTO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="DESCRIPCION",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "DEPTO",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "codarticulo",
                    models.SmallIntegerField(
                        db_column="CODARTICULO", primary_key=True, serialize=False
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="DESCRIPCION",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "PRODUCTO",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Seccion",
            fields=[
                (
                    "numseccion",
                    models.SmallIntegerField(
                        db_column="NUMSECCION", primary_key=True, serialize=False
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="DESCRIPCION",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "SECCION",
                "managed": False,
            },
        ),
    ]