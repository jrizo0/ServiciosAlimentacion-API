# Generated by Django 4.1 on 2022-08-24 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarifav",
            fields=[
                (
                    "idtarifav",
                    models.SmallIntegerField(
                        db_column="IDTARIFAV", primary_key=True, serialize=False
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
                "db_table": "TARIFAV",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Tarifa",
            fields=[
                (
                    "idtarifav",
                    models.OneToOneField(
                        db_column="IDTARIFAV",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="restaurantes.tarifav",
                    ),
                ),
                ("codarticulo", models.SmallIntegerField(db_column="CODARTICULO")),
                ("precio", models.FloatField(db_column="PRECIO")),
            ],
            options={
                "db_table": "TARIFA",
                "managed": False,
            },
        ),
    ]
