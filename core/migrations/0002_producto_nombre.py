# Generated by Django 4.2.1 on 2023-06-06 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default='producto', max_length=200),
        ),
    ]
