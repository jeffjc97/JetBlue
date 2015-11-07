# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Getaway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flight_origin', models.CharField(max_length=10)),
                ('flight_dest', models.CharField(max_length=10)),
                ('hotel', models.CharField(max_length=300)),
                ('nights', models.IntegerField()),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('expedia_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('jetblue_price', models.DecimalField(max_digits=10, decimal_places=1)),
                ('savings', models.DecimalField(max_digits=4, decimal_places=1)),
                ('advance_weeks', models.IntegerField()),
            ],
        ),
    ]
