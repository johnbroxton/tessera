from django.contrib import admin

# Register your models here.

from .models import Image
from .models import Effects
from .models import Ratios

admin.site.register(Image)
admin.site.register(Effects)
admin.site.register(Ratios)
