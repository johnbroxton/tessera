from django.contrib import admin
from .models import UserProfile
from .models import Picture
from .models import Effect
from .models import Ratio

admin.site.register(UserProfile)
admin.site.register(Picture)
admin.site.register(Effect)
admin.site.register(Ratio)
