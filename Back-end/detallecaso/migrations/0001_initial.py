# Generated by Django 3.1.7 on 2021-09-02 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caso', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detallecaso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripccion', models.CharField(max_length=200)),
                ('porcentaje', models.CharField(max_length=200)),
                ('Caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caso.caso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
