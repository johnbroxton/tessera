from django.conf.urls import include, url
from images import views

urlpatterns = [
    url(r'^$', views.images, name='images'),
]