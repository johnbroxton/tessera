# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import users.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinateSystem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('pythagorean', models.BooleanField(default=False)),
                ('square_grid', models.BooleanField(default=False)),
                ('customer_generated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Effect',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('black_and_white', models.BooleanField(default=False)),
                ('color_tint_value', models.BooleanField(default=False)),
                ('color_tint_blue', models.BooleanField(default=False)),
                ('color_tint_red', models.BooleanField(default=False)),
                ('color_tint_green', models.BooleanField(default=False)),
                ('color_tint_yellow', models.BooleanField(default=False)),
                ('color_tint_orange', models.BooleanField(default=False)),
                ('color_tint_purple', models.BooleanField(default=False)),
                ('color_tint_cyan', models.BooleanField(default=False)),
                ('solarize', models.BooleanField(default=False)),
                ('bleach_bypass', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('effects_id', models.ForeignKey(to='users.Effect')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedMosaic',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('coordinate_system', models.ForeignKey(to='users.CoordinateSystem')),
                ('generated_image_id', models.ForeignKey(to='users.GeneratedImage')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PrintMosaic',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('mosaic_id', models.ForeignKey(to='users.GeneratedMosaic')),
            ],
        ),
        migrations.CreateModel(
            name='Ratio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('square', models.BooleanField(default=False)),
                ('golden_ratio_lndscp', models.BooleanField(default=False)),
                ('golden_ratio_port', models.BooleanField(default=False)),
                ('ratio_2_to_3', models.BooleanField(default=False)),
                ('ratio_3_to_2', models.BooleanField(default=False)),
                ('ratio_4_to_5', models.BooleanField(default=False)),
                ('ratio_5_to_4', models.BooleanField(default=False)),
                ('ratio_5_to_7', models.BooleanField(default=False)),
                ('ratio_7_to_5', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('file', models.ImageField(null=True, blank=True, upload_to=users.models.image_upload)),
                ('user_extended', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ratio',
            name='image_id',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='printmosaic',
            name='ratio_id',
            field=models.ForeignKey(to='users.Ratio'),
        ),
        migrations.AddField(
            model_name='picture',
            name='image_id',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='image_id',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='ratios_id',
            field=models.ForeignKey(to='users.Ratio'),
        ),
        migrations.AddField(
            model_name='effect',
            name='image_id',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
