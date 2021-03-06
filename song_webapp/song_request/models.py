import datetime

from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=40, verbose_name='Titel', unique=True)
    album = models.CharField(max_length=40, verbose_name='Album')
    published = models.IntegerField(verbose_name='Erscheinungsjahr', default=0)
    band = models.ForeignKey(Band, verbose_name='Band', on_delete=models.CASCADE)
    lyrics = models.TextField(verbose_name='Lyrics', default='keine')
    info = models.TextField(verbose_name='Info', default='keine')
    archive = models.BooleanField(verbose_name='Archivsong', default=False)

    @property
    def rehearsed_count(self):
        rehearsal_query = Rehearsal.objects.filter(songs__name=self.name)
        if rehearsal_query.exists():
            return rehearsal_query.count()
        else:
            return 0

    @property
    def last_played(self):
        rehearsal_query = Rehearsal.objects.filter(songs__name=self.name)
        if rehearsal_query.exists():
            return rehearsal_query.latest('date').date
        else:
            return 'Nie'

    @property
    def color(self):
        if self.last_played == 'Nie':
            return 'red'
        else:
            days_not_played = datetime.date.today() - self.last_played
        if days_not_played.days < 15:
            return 'green'
        elif 20 > days_not_played.days > 15:
            return 'yellow'
        else:
            return 'orange'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-band']


class Rehearsal(models.Model):
    date = models.DateField(verbose_name='Datum')
    songs = models.ManyToManyField(Song, default=None, verbose_name='Songs')
    in_progress = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-date']
