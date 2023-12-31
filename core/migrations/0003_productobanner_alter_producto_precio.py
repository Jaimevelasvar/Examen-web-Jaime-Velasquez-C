# Generated by Django 4.2.1 on 2023-06-07 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_producto_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoBanner',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('oferta', models.BooleanField()),
                ('imagen', models.CharField(max_length=200)),
                ('nombre', models.CharField(default='producto', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
