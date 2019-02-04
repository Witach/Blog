from django.shortcuts import render
from app.models import Post
from django.utils import timezone
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
