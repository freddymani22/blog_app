from rest_framework import generics
from rest_framework import permissions
# Create your views here.

from blog.models import Post
from .serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]