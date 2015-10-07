from django.db import models
from django.forms import ModelForm

# Create your models here.

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    # pixel_x_dimension = models.IntegerField()
    # pixel_y_dimension = models.IntegerField()
    # date_time_taken = models.DateTimeField()
    # date_time_uploaded = models.DateTimeField()
    # compression = models.CharField(max_length=30)
    # exposure = models.FloatField()
    # f_number = models.FloatField()
    # color_space = models.CharField(max_length=30)

    def __str__(self):
        return self.file.name

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"

class Effects(models.Model):
    image_id = models.ForeignKey(Image)
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

    def __str__(self):
        return self.file.name

class Ratios(models.Model):
    image_id = models.ForeignKey(Image)
    square = models.BooleanField(default=False)
    golden_ratio_lndscp = models.BooleanField(default=False)
    golden_ratio_port = models.BooleanField(default=False)
    ratio_2_to_3 = models.BooleanField(default=False)
    ratio_3_to_2 = models.BooleanField(default=False)
    ratio_4_to_5 = models.BooleanField(default=False)
    ratio_5_to_4 = models.BooleanField(default=False)
    ratio_5_to_7 = models.BooleanField(default=False)
    ratio_7_to_5 = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name

class GeneratedImage(models.Model):
    image_id = models.ForeignKey(Image)
    effects_id = models.ForeignKey(Effects)
    ratios_id = models.ForeignKey(Ratios)

class CoordinateSystem(models.Model):
    pythagorean = models.BooleanField(default=False)
    square_grid = models.BooleanField(default=False)
    customer_generated = models.BooleanField(default=False)

class GeneratedMosaic(models.Model):
    generated_image_id = models.ForeignKey(GeneratedImage)
    coordinate_system = models.ForeignKey(CoordinateSystem)

class PrintMosaic(models.Model):
    mosaic_id = models.ForeignKey(GeneratedMosaic)
    ratio_id = models.ForeignKey(Ratios)







