# Generated by Django 3.2 on 2023-05-04 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
