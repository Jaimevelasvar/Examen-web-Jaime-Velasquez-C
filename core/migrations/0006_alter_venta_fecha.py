# Generated by Django 4.2.2 on 2023-06-23 03:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_venta_detalleventa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 23, 14, 33, 442562)),
        ),
    ]