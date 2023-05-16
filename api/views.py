from rest_framework import generics
from rest_framework import permissions,authentication
from rest_framework.response import Response

# Create your views here.

from blog.models import Post, Comment
from .serializers import PostSerializer, PostCommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    



class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slugs'


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = PostCommentSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        self.post_slug = self.kwargs['slugs']
        return Post.objects.get(slugs=self.post_slug).comment_set.all()


    def perform_create(self, serializer):
        user = self.request.user
        slug = self.kwargs.get('slugs')
        post =  Post.objects.get(slugs=slug)
        serializer.save(user=user, post=post)
    

       