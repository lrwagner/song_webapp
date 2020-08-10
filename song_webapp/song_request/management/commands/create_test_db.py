import datetime

from django.core.management.base import BaseCommand, CommandError

from song_request.models import Song, Band, Rehearsal
from utils import stats


class Command(BaseCommand):
    help = 'Loads Test Data into the Database'

    def handle(self, *args, **options):
    
        data = stats.get_sheets()
        Song.objects.all().delete()
        Band.objects.all().delete()
        Rehearsal.objects.all().delete()

        for _, row in data.iterrows():
            if Band.objects.filter(name=row['band']).exists():
                band = Band.objects.filter(name=row['band']).get()
            else:
                band = Band(name=row['band'])
                band.save()
            
            if Song.objects.filter(name=row.song).exists():
                song = Song.objects.filter(name=row.song).get()
            else:
                song = Song(
                    name=row['song'],
                    band=band,
                    album='album_name',
                    year=0000,
                    info='leer'
                )
                song.save()
            date = datetime.date.fromisoformat(row['date'])
            if Rehearsal.objects.filter(date=date).exists():
                rehearsal = Rehearsal.objects.filter(date=date).get()
            else:
                rehearsal = Rehearsal(date=date.fromisoformat(row['date']))
                rehearsal.save()
            rehearsal.songs.add(song)
            

        self.stdout.write(self.style.SUCCESS('Successfully loaded Testdata "%s" records' % data.shape[0]))