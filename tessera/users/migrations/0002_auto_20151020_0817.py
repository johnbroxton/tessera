# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='image_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='file',
        ),
        migrations.AddField(
            model_name='picture',
            name='file',
            field=models.ImageField(null=True, upload_to=users.models.image_upload, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ManyToManyField(to='users.Picture'),
        ),
    ]
