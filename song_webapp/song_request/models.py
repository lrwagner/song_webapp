from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Song(models.Model):
    # TODO Farbe für Icon anhand Zeitpunkt der letzten Probe
    name = models.CharField(max_length=40, verbose_name='Titel')
    album = models.CharField(max_length=40, verbose_name='Album')
    year = models.IntegerField(verbose_name='Erscheinungsjahr')
    band = models.ForeignKey(Band, verbose_name='Band', on_delete=models.CASCADE)
    info = models.TextField(verbose_name='Info')

    def __str__(self):
        return self.name

class Rehearsal(models.Model):
    date = models.DateField(verbose_name='Datum')
    songs = models.ManyToManyField(Song, verbose_name='Songs')