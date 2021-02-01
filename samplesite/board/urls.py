from django.urls import path, include
from .views import (index, by_rubric, BoardCreateView, show_user_posts)


urlpatterns = [
    path('add/', BoardCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('user_posts/', show_user_posts, name='user_posts')
]
