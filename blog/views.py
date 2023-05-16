from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
ListView, 
DetailView,
CreateView,
UpdateView,
DeleteView)
from .models import Post
from .forms import CommentForm
from .models import Comment 








class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/home1.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5



class UserPostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return user.post_set.all().order_by('-date_posted')
        # return Post.objects.filter(author = user).order_by('-date_posted')
        



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    form = CommentForm
    slug_field = 'slugs'
    slug_url_kwarg = 'slugs'
    template_name = 'blog/post_detail1.html'




    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'img_post']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'img_post']
  
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    success_url = '/'
    
    


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})