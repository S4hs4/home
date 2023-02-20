from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

def index(request):
    films = Film.objects.all()

    form = FilmForm()

    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'films':films, 'form':form}
    return render(request, 'home.html', context)
def editFilm(request, pk):
    film = Film.objects.get(id=pk)

    form = FilmForm(instance=film)

    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'update_film.html', context)

def deleteFilm(request, pk):
    item = Film.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}

    return render(request, 'delete.html', context)