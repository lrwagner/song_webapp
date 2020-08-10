from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    # TODO Farbe für Icon anhand Zeitpunkt der letzten Probe
    name = models.CharField(max_length=40, verbose_name='Titel', unique=True)
    album = models.CharField(max_length=40, verbose_name='Album')
    year = models.IntegerField(verbose_name='Erscheinungsjahr')
    band = models.ForeignKey(Band, verbose_name='Band', on_delete=models.CASCADE)
    info = models.TextField(verbose_name='Info')

    @property
    def last_played(self):
        rehearsal_query = Rehearsal.objects.filter(songs__name=self.name)
        if rehearsal_query.exists():
            return rehearsal_query.latest('date').date
        else:
            return 'noch nie gespielt!'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-band']


class Rehearsal(models.Model):
    date = models.DateField(verbose_name='Datum')
    songs = models.ManyToManyField(Song, verbose_name='Songs')

    def __str__(self):
        return str(self.date)
    
    class Meta:
        ordering = ['-date']