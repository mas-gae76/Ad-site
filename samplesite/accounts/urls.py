from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import path


urlpatterns = [
    url('change_password/', views.change_password, name='change_password'),
    url('logout/', views.logout_view, name='logout'),
    path('login/', views.user_login, name='login'),
    url('register/', views.register, name='register'),
    url('profile/', views.show_person_cabinet, name='profile'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('reset_password/', views.password_reset, name='reset_password'),
    path('done/', views.password_reset_done, name='password_reset_done'),
]
