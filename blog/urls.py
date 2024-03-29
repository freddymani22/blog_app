from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog-home"),
    path('post/new/', views.PostCreateView.as_view(), name="post-create"),
    path('user/<str:username>/', views.UserPostListView.as_view(), name="user-posts"),
    path('post/<slug:slugs>/', views.PostDetailView.as_view(), name="post-detail"),
    path('post/<slug:slugs>/update/', views.PostUpdateView.as_view(), name="post-update"),
    path('post/<slug:slugs>/delete/', views.PostDeleteView.as_view(), name="post-delete"),
    path('about/', views.about, name="blog-about"),

]
