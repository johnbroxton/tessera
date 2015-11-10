from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    url(r'^$', 'users.views.index', name='index'),
    url(r'^login/$', 'users.views.user_login', name='login'),
    url(r'^logout/$', 'users.views.log_out', name='logout'),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^upload/$', 'users.views.upload', name='upload'),
    url(r'^about/$', 'users.views.about', name='about'),
    url(r'^mosaic/(?P<pk>[0-9]+)/$', 'users.views.profile', name='mosaic'),


    url(r'^admin/', include(admin.site.urls)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

