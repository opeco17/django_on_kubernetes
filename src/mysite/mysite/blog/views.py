from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.views.generic import View

from .models import Post
from .forms import PostForm
from .utils import login_user_is_writer


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
        context = {'posts': posts}
        return render(request, 'blog/post_list.html', context)


class PostDetailView(View):
    def get(self, request, post_id, *args, **kwargs):
        post = Post.objects.get(id=post_id)
        editable = login_user_is_writer(request.user, post.writer)
        context = {'post': post, 'editable': editable}
        return render(request, 'blog/post_detail.html', context)


class PostEditView(View):
    def get(self, request, post_id, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, '編集にはログインが必要です', extra_tags='danger')
            return redirect('account_login')
        
        post = Post.objects.get(id=post_id)
        if not login_user_is_writer(request.user, post.writer):
            messages.error(request, '投稿者のみ編集が可能です', extra_tags='danger')
            return redirect('post_detail', post_id=post_id)
        
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(instance=post)
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, post_id, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, '編集にはログインが必要です', extra_tags='danger')
            return redirect('account_login')
        
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)


class PostNewView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, '新規投稿にはログインが必要です', extra_tags='danger')
            return redirect('account_login')
        
        form = PostForm()
        context = {'form': form}
        return render(request, 'blog/post_edit.html', context)
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, '新規投稿にはログインが必要です', extra_tags='danger')
            return redirect('account_login')
        
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.id)