from django.contrib import admin
from song_request.models import Song, Band, Rehearsal

# Register your models here.
admin.site.register(Song)
admin.site.register(Band)
admin.site.register(Rehearsal)