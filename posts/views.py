from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class PostListView(generic.ListView):
    model  = Post
    template_name = "List.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "Detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "Create.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("posts:detail", kwargs={"pk":self.object.pk})







