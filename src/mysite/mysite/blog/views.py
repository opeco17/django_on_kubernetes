from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View
from .models import Post
from .forms import PostForm


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context = {'posts': posts}
        return render(request, 'blog/post_list.html', context)


post_list = PostListView.as_view()


class PostDetailView(View):
    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        context = {'post': post}
        return render(request, 'blog/post_detail.html', context)


post_detail = PostDetailView.as_view()


class PostNewView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=1)


post_new = PostNewView.as_view()


class PostEditView(View):
    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    

post_edit = PostEditView.as_view()