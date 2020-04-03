from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

# posts = [
#     {
#         'author': 'Qian', 
#         'title': 'Blog 1: ML',
#         'content': 'Machine Learning',
#         'date_posted': 'March 31, 2020',
#     },
#     {
#         'author': 'Chen', 
#         'title': 'Blog 2: CV',
#         'content': 'Computer Vision',
#         'date_posted': 'March 31, 2020',
#     }
# ]

def home(request): # handle the traffic from home page.
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # then home.html can access posts by the key 'posts'


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request): # about page
    return render(request, 'blog/about.html', {'title': 'About'})