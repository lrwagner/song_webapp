from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count

from song_request import models
from .forms import RehearsalForm


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


def create_rehearsal_view(request):

    if models.Rehearsal.objects.filter(in_progress=True).exists():
        rehearsal = models.Rehearsal.objects.filter(in_progress=True).get()

        if request.method == 'POST':
            form = RehearsalForm(request.POST)
            song_name = form.data['song_name']
            song = models.Song.objects.filter(name=song_name).get()
            rehearsal.songs.add(song)
            songs = rehearsal.songs.all()

        else:
            songs = rehearsal.songs.all()
    else:
        today = date.today()
        rehearsal = models.Rehearsal(date=today, in_progress=True)
        rehearsal.save()
        songs = None

    context = {
        'form': RehearsalForm(),
        'rehearsal': rehearsal,
        'songs': songs
        }
    return render(request, 'song_request/create_rehearsal.html', context)


def rehearsal_del_song(request, rehearsal, song):
    rehearsal = get_object_or_404(models.Rehearsal, pk=rehearsal)
    song = get_object_or_404(models.Song, pk=song)

    if request.method == 'POST':
        rehearsal.songs.remove(song)
        return redirect('create_rehearsal')

    return redirect('create_rehearsal')


def submit_rehearsal(request, rehearsal):
    rehearsal = get_object_or_404(models.Rehearsal, pk=rehearsal)
    rehearsal.in_progress = False
    rehearsal.save()

    return redirect('create_rehearsal')
