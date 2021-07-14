from django.conf.urls import url
from . import views

from django.conf.urls import url
from . import views
from accounts.views import registerPage, loginPage, logoutUser, contact

urlpatterns = [
    url('register/', registerPage, name='register'),
    url('login/', loginPage, name='login'),
    url('logout/', logoutUser, name='logout'),
    url(r'contact/', contact, name='contact'),
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'research/(?P<exchange>[\w-]+)/$', views.research, name='research'),
    url(r'reports/(?P<slug>[\w-]+)/$', views.reports, name='reports'),
    url(r'research/', views.nse, name='nse'),
    url(r'products/(?P<exchange>[\w-]+)/$', views.products, name='products'),
    url(r'services/', views.services, name='services'),
    url(r'nse_losers/', views.get_nse_losers, name='nse_losers'),
    url(r'nse_gainers/', views.get_nse_gainers, name='nse_gainers'),
    url(r'bse_losers/', views.get_bse_losers, name='bse_losers'),
    url(r'bse_gainers/', views.get_bse_gainers, name='bse_gainers'),
    url(r'nasdaq_losers/', views.get_nasdaq_losers, name='nasdaq_losers'),
    url(r'nasdaq_gainers/', views.get_nasdaq_gainers, name='nasdaq_gainers'),
    url(r'blogs/', views.PostList, name='post'),
    url(r'blog/(?P<slug>[\w-]+)/$', views.PostDetail, name='post_detail')
]