from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from .models import *

class PostList(ListView):
    model = Post
    context_object_name = 'Posts'
    template_name = 'news/post_list.html'
    queryset = Post.objects.all().order_by('-pk')


class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/authors.html'
    queryset = Author.objects.all()

class Post(DetailView):
    model = Post
    context_object_name = 'Post'
    template_name = 'news/post_detail.html'
