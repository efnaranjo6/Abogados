# Generated by Django 3.0.4 on 2020-06-22 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_persona_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='user',
        ),
    ]
