from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

def image_upload(instance, filename):
    return 'images/{}/{}'.format(instance.user.username, filename)

class Picture(models.Model):
    file = models.ImageField(upload_to=image_upload, blank=True, null=True)
    user = models.ForeignKey(User)

class UserProfile(models.Model):
    user_extended = models.OneToOneField(User)

    def __str__(self):
        return self.user_extended.username


class Effect(models.Model):
    image_id = models.ForeignKey(UserProfile)
    black_and_white = models.BooleanField(default=False)
    color_tint_value = models.BooleanField(default=False)
    color_tint_blue = models.BooleanField(default=False)
    color_tint_red = models.BooleanField(default=False)
    color_tint_green = models.BooleanField(default=False)
    color_tint_yellow = models.BooleanField(default=False)
    color_tint_orange = models.BooleanField(default=False)
    color_tint_purple = models.BooleanField(default=False)
    color_tint_cyan = models.BooleanField(default=False)
    solarize = models.BooleanField(default=False)
    bleach_bypass = models.BooleanField(default=False)


class Ratio(models.Model):
    image_id = models.ForeignKey(UserProfile)
    square = models.BooleanField(default=False)
    golden_ratio_lndscp = models.BooleanField(default=False)
    golden_ratio_port = models.BooleanField(default=False)
    ratio_2_to_3 = models.BooleanField(default=False)
    ratio_3_to_2 = models.BooleanField(default=False)
    ratio_4_to_5 = models.BooleanField(default=False)
    ratio_5_to_4 = models.BooleanField(default=False)
    ratio_5_to_7 = models.BooleanField(default=False)
    ratio_7_to_5 = models.BooleanField(default=False)


class GeneratedImage(models.Model):
    image_id = models.ForeignKey(UserProfile)
    effects_id = models.ForeignKey(Effect)
    ratios_id = models.ForeignKey(Ratio)


class GeneratedMosaic(models.Model):
    generated_image_id = models.ForeignKey(GeneratedImage)

class PrintMosaic(models.Model):
    mosaic_id = models.ForeignKey(GeneratedMosaic)
    ratio_id = models.ForeignKey(Ratio)