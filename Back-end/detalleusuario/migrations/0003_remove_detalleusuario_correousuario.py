# Generated by Django 3.0.4 on 2021-04-22 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalleusuario', '0002_detalleusuario_correousuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleusuario',
            name='correoUsuario',
        ),
    ]
