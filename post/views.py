from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse


def article(request):
    posts = Post.objects.all()
    return render(request, 'post/article.html', {'posts': posts})


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/post/')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/new.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post/detail.html', {'post': post})


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/post/')


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post/edit.html', {'post': post})


def update(request, pk):
    post = Post.objects.get(pk=pk)
    title = request.GET.get('title')
    body = request.GET.get('content')

    post.title = title
    post.body = body

    post = Post(title=title, body=body)
    post.save()

    return redirect('/post/')
