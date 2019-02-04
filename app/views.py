from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from app.models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
class startView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by("-published_date")

class PostDetailView(DetailView):
    model = Post

class PoostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    login_url='/login/'
    redirect_field_name = "post_detail.html"
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    login_url='/login/'
    redirect_field_name = "post_detail.html"
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    login_url='/login/'
    succes_url="post_list"
