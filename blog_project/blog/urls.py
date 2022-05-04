from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='blog-create'),
]
