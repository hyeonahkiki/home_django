from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method =='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'posts/form.html', context)

def detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment_form = CommentForm()
    context = {
        'post':post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)

def update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method=='POST':
        # 과거의 데이터는 instance로 저장하기
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', id)
    else:
        # 과거의 데이터는 instance로 저장하기
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'posts/form.html', context)

def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('posts:index')

def comment_create(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method =='POST':
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', id)

def comment_delete(request, post_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('posts:detail', post_id)

def like(request, id):
    post = get_object_or_404(Post, id=id)
    user = request.user
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:detail', id)