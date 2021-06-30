# Generated by Django 3.0.4 on 2021-04-22 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0005_auto_20210419_1516'),
        ('rol', '0002_rol_nombrerol'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detalleusuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rol.Rol')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
