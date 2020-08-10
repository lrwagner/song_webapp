from django.shortcuts import render
from django.db.models import Count
from song_request import models

def song_view(request):

    context = {
        'songs': models.Song.objects.all()
    }
    return render(request, 'song_request/songs.html', context)


def band_view(request):

    context = {
        'bands': models.Band.objects.all()
    }
    return render(request, 'song_request/bands.html', context)


def rehearsal_view(request):

    context = {
        'rehearsals': models.Rehearsal.objects.all()[:3],
        'song_counts': models.Song.objects.annotate(Count('rehearsal')).order_by('-rehearsal__count')[:10]
    }
    return render(request, 'song_request/rehearsals.html', context)