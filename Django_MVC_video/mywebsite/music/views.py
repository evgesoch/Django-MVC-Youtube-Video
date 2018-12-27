from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album
from django.template import loader

# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    template = 'music/index.html'
    context = {
        'all_albums':all_albums
    }
    return render(request, template, context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})