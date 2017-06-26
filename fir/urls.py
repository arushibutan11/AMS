from django.conf.urls import url

#from . import views
from django.views import generic
from django.views.generic.edit import CreateView
from fir import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^$', views.create_fir2, name='create_fir'),
    url(r'^getcircleinfo$', views.getcircleinfo, name='getcircleinfo'),
    url(r'^getsection$', views.getsection, name='getsection'),
    url(r'^getlocation$', views.getlocation, name='getlocation'),
    url(r'^getacctype$', views.getacctype, name='getacctype'),
    url(r'^signup/$', views.signup, name='signup')
]
