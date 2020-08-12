from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponseRedirect

from song_request import models
from .forms import NameForm


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
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/probe/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'song_request/create_rehearsal.html', {'form': form})