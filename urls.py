from django.conf.urls import patterns, url
from convertPixelArt import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^convertImages.html$', views.changePicture, name ='convertImages'),
)

