from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=40)


class Song(models.Model):
    name = models.CharField(max_length=40, verbose_name='Titel')
    album = models.CharField(max_length=40, verbose_name='Album')
    year = models.DateField(verbose_name='Erscheinungsjahr')
    band = models.ForeignKey(Band, verbose_name='Band', on_delete=models.CASCADE)


class Rehearsal(models.Model):
    date = models.DateField(verbose_name='Datum')
    songs = models.ManyToManyField(Song, verbose_name='Songs')