from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('login/login.html', views.user_login, name='login'),
    url('register/register.html', views.register, name='register'),
]
