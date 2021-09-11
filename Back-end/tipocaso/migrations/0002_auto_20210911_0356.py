# Generated by Django 3.1.7 on 2021-09-11 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tipocaso', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipocaso',
            options={'verbose_name': 'modelo base', 'verbose_name_plural': 'BaseModels'},
        ),
        migrations.AddField(
            model_name='tipocaso',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Fecha de creacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipocaso',
            name='delete_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de elimnacion'),
        ),
        migrations.AddField(
            model_name='tipocaso',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificacion'),
        ),
        migrations.AddField(
            model_name='tipocaso',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='tipocaso',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
