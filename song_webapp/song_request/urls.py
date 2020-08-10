from django.urls import path

from song_request import views


urlpatterns = [
    path('songs', views.song_view, name='songs'),
    path('bands', views.band_view, name='bands'),
    path('proben', views.rehearsal_view, name='proben')
]