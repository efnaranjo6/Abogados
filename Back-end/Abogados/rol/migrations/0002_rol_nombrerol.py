# Generated by Django 3.0.4 on 2020-05-25 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rol', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='nombreRol',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]