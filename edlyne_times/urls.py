from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'research/', views.research, name='research'),
    url(r'reports/', views.reports, name='reports'),
    url(r'research/', views.nse, name='nse'),
]