from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('boards', views.BoardViewSet)

urlpatterns = [
    path('boards/', views.BoardListView.as_view(), name='board_list'),
    path('boards/<pk>/', views.BoardDetailView.as_view(), name='board_detail'),
    path('', include(router.urls)),
]