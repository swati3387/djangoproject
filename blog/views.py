from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post


# Create your views here.
def post_list(request):
    # return HttpResponse("<b>Here's the text of the Web page.</b>")
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    # return HttpResponse("<b>Here's the text of the Web page.</b>")
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm()
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'blog/post_edit.html', context)


@login_required
def post_draft_list(request):
    # posts= Post.objects.filter()
    # context={"posts": posts}
    # return render(request,'blog/post_draft_list.html',context)
    posts = Post.objects.filter(published_date__isnull=True)
    context = {"posts": posts}
    return render(request, 'blog/post_draft_list.html', context)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.published_date = timezone.now()
    post.save()
    return redirect('post_detail', pk=pk)


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
