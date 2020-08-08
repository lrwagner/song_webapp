from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=40)
    album = models.CharField(max_length=40)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)


class Band(models.Model):
    name = models.CharField(max_length=40)


class Rehearsal(models.Model):
    date = models.DateField()
    songs = models.ManyToManyField(Song)