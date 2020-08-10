from django.urls import path

from song_request import views


urlpatterns = [
    path('', views.song_view, name='song_view')
]