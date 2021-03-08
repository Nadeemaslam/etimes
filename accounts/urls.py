from django.conf.urls import url
from . import views
from accounts.views import registerPage, loginPage, logoutUser

urlpatterns = [
    url('register/', registerPage, name='register'),
    url('login/', loginPage, name='login'),
    url('logout/', logoutUser, name='logout')
]