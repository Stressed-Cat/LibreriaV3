# Generated by Django 4.0.5 on 2022-07-03 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0010_articulo_presencial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccionentrega',
            name='fecha_entrega',
            field=models.DateTimeField(null=True),
        ),
    ]
