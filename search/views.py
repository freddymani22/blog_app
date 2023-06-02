from rest_framework import generics

# Create your views here.
from blog.models import Post
from api.serializers import PostSerializer

class PostSearchApi(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        results = Post.objects.none()  
        if q is not None:

         return qs.search(query = q)

        return results
