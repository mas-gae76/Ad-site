from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_ad, name='add'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('user_posts/', views.show_user_posts, name='user_posts'),
    path('search/', views.search, name='post_search'),
    path('delete_ad/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('edit_ad/<int:ad_id>/', views.edit_ad, name='edit_ad'),
    path('user_profile/<int:user_id>/', views.show_user_profile, name='user_profile'),
]
