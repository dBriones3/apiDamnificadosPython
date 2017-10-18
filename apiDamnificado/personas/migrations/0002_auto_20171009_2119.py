# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-10 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personas',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='personas',
            name='tipo_de_personas',
            field=models.CharField(choices=[('Voluntario', 'Voluntario'), ('Damnificado', 'Damnificado'), ('Otro', 'Otro')], max_length=50),
        ),
    ]
