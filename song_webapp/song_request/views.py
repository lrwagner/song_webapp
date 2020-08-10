from django.shortcuts import render
from song_request import models

def song_view(request):

    context = {
        'songs': models.Song.objects.all()
    }
    return render(request, 'song_request/index.html', context)