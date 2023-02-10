from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse


def home(request):
    return render(request, 'forum/home.html')

def article(request):
    posts = Post.objects.all()
    return render(request, 'forum/article.html', {'posts': posts})


def new(request):
    print("new")
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/forum/')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'forum/new.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'forum/detail.html', {'post': post})


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/forum/')


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'forum/edit.html', {'post': post})


def update(request, pk):
    post = Post.objects.get(pk=pk)
    title = request.GET.get('title')
    body = request.GET.get('content')

    post.title = title
    post.body = body

    post = Post(title=title, body=body)
    post.save()

    return redirect('/forum/')
