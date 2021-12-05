import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def spotify():
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    return sp

def get_artist_id(sp,artist):
    results = sp.search(q='artist:' + artist, type='artist',limit=20)
    for item in results['artists']['items']:
        if item['name'].lower() == artist.lower():
            id =item["id"]
            break
    return id

def get_relate_artists_songs(sp,id):
    relate_atrists_dic = {}
    results = sp.artist_related_artists(id)
    results_artists = results['artists']
    for i in range(len(results_artists)):
        relate_artist = results_artists[i]['name']
        relate_artist_id = results_artists[i]['id']
        relate_artist_results = sp.artist_top_tracks(relate_artist_id)
        results_tracks = relate_artist_results["tracks"]
        for x in results_tracks:
            top_song = x["album"]["artists"][0]["external_urls"]["spotify"]
            relate_atrists_dic[relate_artist] = top_song
    return relate_atrists_dic


def execute_relate_method(artist):
    sp = spotify()
    id = get_artist_id(sp,artist)
    relate_artists_dic = get_relate_artists_songs(sp,id)
    print(relate_artists_dic)
    return relate_artists_dic

def get_feature_playlists(sp):
    feature_playlists_dic = {}
    results = sp.featured_playlists(country="JP")
    results_playlists = results["playlists"]["items"]
    for i in results_playlists:
        print(i["description"],i["external_urls"]["spotify"])
        description,playlist = i["description"],i["external_urls"]["spotify"]
        feature_playlists_dic[description] = playlist
    return feature_playlists_dic

def execute_feature_method():
    sp = spotify()
    feature_playlists_dic = get_feature_playlists(sp)
    print(feature_playlists_dic)
    return feature_playlists_dic
