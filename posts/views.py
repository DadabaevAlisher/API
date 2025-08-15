from django.shortcuts import render
from .models import Post
from django.views import generic
# Create your views here.


class PostListView(generic.ListView):
    model  = Post
    template_name = "List.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "Detail.html"
    context_object_name = "post"


class PostCreateView(generic.CreateView):
    model = Post
    template_name = "Create.html"
    context_object_name = "post"






