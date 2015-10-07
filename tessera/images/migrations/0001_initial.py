# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoordinateSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('pythagorean', models.BooleanField(default=False)),
                ('square_grid', models.BooleanField(default=False)),
                ('customer_generated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Effects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('effects_id', models.ForeignKey(to='images.Effects')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedMosaic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('coordinate_system', models.ForeignKey(to='images.CoordinateSystem')),
                ('generated_image_id', models.ForeignKey(to='images.GeneratedImage')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.ImageField(upload_to='')),
                ('pixel_x_dimension', models.IntegerField()),
                ('pixel_y_dimension', models.IntegerField()),
                ('date_time_taken', models.DateTimeField()),
                ('date_time_uploaded', models.DateTimeField()),
                ('compression', models.CharField(max_length=30)),
                ('exposure', models.FloatField()),
                ('f_number', models.FloatField()),
                ('color_space', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PrintMosaic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('mosaic_id', models.ForeignKey(to='images.GeneratedMosaic')),
            ],
        ),
        migrations.CreateModel(
            name='Ratios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('square', models.BooleanField(default=False)),
                ('golden_ratio_lndscp', models.BooleanField(default=False)),
                ('golden_ratio_port', models.BooleanField(default=False)),
                ('ratio_2_to_3', models.BooleanField(default=False)),
                ('ratio_3_to_2', models.BooleanField(default=False)),
                ('ratio_4_to_5', models.BooleanField(default=False)),
                ('ratio_5_to_4', models.BooleanField(default=False)),
                ('ratio_5_to_7', models.BooleanField(default=False)),
                ('ratio_7_to_5', models.BooleanField(default=False)),
                ('image_id', models.ForeignKey(to='images.Image')),
            ],
        ),
        migrations.AddField(
            model_name='printmosaic',
            name='ratio_id',
            field=models.ForeignKey(to='images.Ratios'),
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='image_id',
            field=models.ForeignKey(to='images.Image'),
        ),
        migrations.AddField(
            model_name='generatedimage',
            name='ratios_id',
            field=models.ForeignKey(to='images.Ratios'),
        ),
        migrations.AddField(
            model_name='effects',
            name='image_id',
            field=models.ForeignKey(to='images.Image'),
        ),
    ]
