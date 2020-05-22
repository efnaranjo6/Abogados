# Generated by Django 3.0.4 on 2020-05-22 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detallecaso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripccion', models.CharField(max_length=200)),
                ('porcentaje', models.CharField(max_length=200)),
                ('Caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caso.Caso')),
            ],
        ),
    ]
