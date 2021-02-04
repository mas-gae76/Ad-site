from django.urls import path
from .views import (index, by_rubric, add_ad, show_user_posts, search)


urlpatterns = [
    path('add/', add_ad, name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('user_posts/', show_user_posts, name='user_posts'),
    path('search/', search, name='post_search')
]
