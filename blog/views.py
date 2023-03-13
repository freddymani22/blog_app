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



def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)




class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/home.html'
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
        return Post.objects.filter(author = user).order_by('-date_posted')
        

        


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    form = CommentForm



    def get(self, request, *args, **kwargs):
        context ={}
        self.object = self.get_object()
        # print(self.object.title)
        context = self.get_context_data(object=self.object)
        print(context['object'])
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return self.render_to_response(context)
    

    def post(self, request):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.user = request.user
            comment.save()
            return redirect('post-detail', pk = self.object.pk)





    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.image = self.request.FILES.get('image')
        form.save()
        return redirect('blog-home')


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
  
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