from django.shortcuts import render
from .models import Post
from django.views.generic import *
# Create your views here.


class PostListView(ListView):
    model  = Post
    template_name = "List.html"
    context_object_name = "posts"

    


