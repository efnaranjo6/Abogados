# Generated by Django 3.0.4 on 2020-06-20 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_persona_user'),
        ('usuariocaso', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariocaso',
            name='Usuario',
        ),
        migrations.AddField(
            model_name='usuariocaso',
            name='Persona',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='persona.Persona'),
            preserve_default=False,
        ),
    ]
