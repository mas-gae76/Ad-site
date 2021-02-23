from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_ad, name='add'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('', views.index, name='index'),
    path('user_posts/', views.show_user_posts, name='user_posts'),
    path('search/', views.search, name='post_search'),
    path('delete_ad/<int:ad_id>/', views.delete_ad, name='delete_ad'),
    path('edit_ad/<int:ad_id>/', views.edit_ad, name='edit_ad'),
]
