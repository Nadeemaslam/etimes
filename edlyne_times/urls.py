from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'research/(?P<exchange>[\w-]+)/$', views.research, name='research'),
    url(r'reports/(?P<slug>[\w-]+)/$', views.reports, name='reports'),
    url(r'research/', views.nse, name='nse'),
    url(r'products/(?P<exchange>[\w-]+)/$', views.products, name='products'),
    url(r'services/', views.services, name='services'),
    url(r'nse_losers/', views.get_nse_losers, name='nse_losers'),
    url(r'nse_gainers/', views.get_nse_gainers, name='nse_gainers'),
    url(r'bse_losers/', views.get_bse_losers, name='bse_losers'),
    url(r'bse_gainers/', views.get_bse_gainers, name='bse_gainers'),
]