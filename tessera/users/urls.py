from django.conf.urls import include, url
from users import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.profile, name='user_profile'),
]