# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20150930_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='color_space',
        ),
        migrations.RemoveField(
            model_name='image',
            name='compression',
        ),
        migrations.RemoveField(
            model_name='image',
            name='date_time_taken',
        ),
        migrations.RemoveField(
            model_name='image',
            name='date_time_uploaded',
        ),
        migrations.RemoveField(
            model_name='image',
            name='exposure',
        ),
        migrations.RemoveField(
            model_name='image',
            name='f_number',
        ),
        migrations.RemoveField(
            model_name='image',
            name='pixel_x_dimension',
        ),
        migrations.RemoveField(
            model_name='image',
            name='pixel_y_dimension',
        ),
    ]
