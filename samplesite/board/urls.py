from django.urls import path
from django.contrib.auth import views
from django.contrib import admin
from django.conf.urls import include, url
from .views import index, by_rubric, BoardCreateView


urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('add/', BoardCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
