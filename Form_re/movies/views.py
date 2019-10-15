from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie,Comment
from .forms import MovieModelForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    comment_form = CommentForm()
    context = {
        'movie':movie,
        'comment_form':comment_form,
    }
    return render(request, 'detail.html', context)

def delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect('movies:index')

def create(request):
    if request.method =='POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movies = form.save()
            return redirect('movies:index')
    else:
        form = MovieModelForm()
    context = {
        'form':form,
    }
    return render(request, 'form.html', context)

def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method =='POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.id)
    else:
        form = MovieModelForm(instance=movie)
    context ={
        'form':form,
    }
    return render(request, 'form.html', context)

def comment_create(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movies:detail', id)
        else:
            pass
    else:
        pass