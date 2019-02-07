from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse_lazy
from app.models import Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from app.form import PostForm,CommentForm
from app.models import Comments,Post
# Create your views here.
class startView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(date_published__lte=timezone.now()).order_by("-date_published")

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
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
    success_url=reverse_lazy("post_list")

class PostDraftListView(LoginRequiredMixin,ListView):
    model = Post
    login_url='/login/'

    def get_queryset(self):
        return Post.objects.filter(date_published__isnull=True).order_by("-date_created")

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment =get_object_or_404(Comments, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comments, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
