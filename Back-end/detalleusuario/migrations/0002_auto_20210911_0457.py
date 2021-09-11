# Generated by Django 3.1.7 on 2021-09-11 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('detalleusuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleusuario',
            options={'verbose_name': 'modelo base', 'verbose_name_plural': 'BaseModels'},
        ),
        migrations.AddField(
            model_name='detalleusuario',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detalleusuario',
            name='delete_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de elimnacion'),
        ),
        migrations.AddField(
            model_name='detalleusuario',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion'),
        ),
        migrations.AddField(
            model_name='detalleusuario',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='detalleusuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
