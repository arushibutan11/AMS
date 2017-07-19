from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#from . import views
from django.views import generic
from django.views.generic.edit import CreateView
from fir import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^home', views.home, name='home'),
    url(r'^$', views.create_fir, name='create_fir'),
    url(r'^newfir$', views.new_fir, name='new_fir'),
    url(r'^search_fir$', views.search_fir, name='search_fir'),
    url(r'^edit_fir/(?P<acc_id>[\w]+)/$', views.edit_fir, name='edit_fir'),
    url(r'^getcircleinfo$', views.getcircleinfo, name='getcircleinfo'),
    url(r'^getsection$', views.getsection, name='getsection'),
    url(r'^getlocation$', views.getlocation, name='getlocation'),
    url(r'^getacctype$', views.getacctype, name='getacctype'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^report/(?P<month>[0-9]+)/(?P<year>[0-9]+)/(?P<fn>[0-9]+)', views.report_acc_type, name='report_acc_type'),
]

	#url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html', 'next_page': '/'}, name='logout'),]
