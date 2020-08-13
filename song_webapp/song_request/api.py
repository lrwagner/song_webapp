import requests

from song_request._api_secrets import API_KEY
from song_request.models import Song, Band

URL = f'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}'

def get_song_meta(songname):
    """ json response: ['name', 'mbid', 'url', 'duration', 'streamable', 'listeners', 'playcount', 'artist', 'album', 'toptags', 'wiki']
    """
    band = Song.objects.filter(name=songname.lower()).get().band
    r = requests.post(URL + f'&artist={band}&track={songname}&format=json')
    info_json = r.json()['track']
    return info_json