from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'research/(?P<exchange>[\w-]+)/$', views.research, name='research'),
    url(r'reports/(?P<slug>[\w-]+)/$', views.reports, name='reports'),
    url(r'research/', views.nse, name='nse'),
]