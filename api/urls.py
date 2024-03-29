from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import PostListCreateView, PostDetailView, CommentListCreateView

urlpatterns = [
    path('auth/',obtain_auth_token),
    path('',PostListCreateView.as_view(), name='api-home'),
    path('search/',include('search.urls')),
    path('<slug:slugs>/',PostDetailView.as_view(), name='api-detail'),
    path('comments/<slug:slugs>/',CommentListCreateView.as_view(), name='api-comments'),
    path('comments/<slug:slugs>/',CommentListCreateView.as_view(), name='api-comments'),
]