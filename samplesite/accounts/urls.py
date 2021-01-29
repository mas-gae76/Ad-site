from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url('change_password/', views.changePassword, name='change_password'),
    url('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    url('register/', views.register, name='register'),
]
