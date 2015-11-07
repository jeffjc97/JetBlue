# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getaway',
            name='advance_weeks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='getaway',
            name='expedia_price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='getaway',
            name='jetblue_price',
            field=models.DecimalField(max_digits=10, decimal_places=1),
        ),
    ]
