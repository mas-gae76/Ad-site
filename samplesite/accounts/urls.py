from django.conf.urls import url
from . import views


urlpatterns = [
    url('board/login/', views.user_login, name='login'),
]
