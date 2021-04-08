from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'research/', views.research, name='research'),
    url(r'nse/', views.nse, name='nse'),
    url(r'tsx_gainers/', views.tsx_gainers, name='tsx_gainers'),
    url(r'tsx_losers/', views.tsx_losers, name='tsx_losers'),
    url(r'nyse_losers/', views.get_nyse_losers, name='nyse_losers'),
    url(r'nyse_gainers/', views.get_nyse_gainers, name='nyse_gainers'),
]