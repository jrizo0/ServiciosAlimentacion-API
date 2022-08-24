# Generated by Django 4.1 on 2022-08-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "codcliente",
                    models.SmallIntegerField(
                        db_column="CODCLIENTE", primary_key=True, serialize=False
                    ),
                ),
                (
                    "nombrecliente",
                    models.CharField(
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="NOMBRECLIENTE",
                        max_length=50,
                    ),
                ),
                (
                    "direccion1",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="DIRECCION1",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "e_mail",
                    models.CharField(
                        db_collation="Latin1_General_100_CS_AI_SC_UTF8",
                        db_column="E_MAIL",
                        max_length=50,
                    ),
                ),
            ],
            options={
                "db_table": "CLIENTE",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Tipocliente",
            fields=[
                (
                    "idtipo",
                    models.SmallIntegerField(
                        db_column="IDTIPO", primary_key=True, serialize=False
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
                "db_table": "TIPOCLIENTE",
                "managed": False,
            },
        ),
    ]
