from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View
from .models import Post
from .forms import PostForm


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
        context = {'posts': posts}
        return render(request, 'blog/post_list.html', context)


post_list = PostListView.as_view()


class PostDetailView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.filter(id=post_id).first()
        context = {'post': post}
        return render(request, 'blog/post_detail.html', context)


post_detail = PostDetailView.as_view()


class PostEditView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)

post_edit = PostEditView.as_view()


class PostNewView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)
          

post_new = PostNewView.as_view()