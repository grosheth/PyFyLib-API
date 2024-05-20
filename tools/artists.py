import spotipy
from tools.authentication import login

def get_artist_id(artist: str, track: str):
    spotify = login()

    track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track')
    songs_info = {}
 
    for index, content in enumerate(track_id['tracks']['items']): 
        song_info = {index: {'artist': content['artists'][0]['name'], 'track': content['name'],'id': content['id'] }}
        songs_info.update(song_info)

    print(songs_info)

    return songs_info
# def get_top10(artist=None, artist_id=None):
#     lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
#
#     spotify = login()
#     results = spotify.artist_top_tracks(lz_uri)
#
#     for track in results['tracks'][:10]:
#         print('track    : ' + track['name'])
#         print('audio    : ' + track['preview_url'])
#         print('cover art: ' + track['album']['images'][0]['url'])
#         print()
#
#     return {"top10"}
#
# def get_song(artist=None, artist_id=None):
#     birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
#
#     spotify = login()
#     results = spotify.artist_albums(birdy_uri, album_type='album')
#     albums = results['items']
#     while results['next']:
#         results = spotify.next(results)
#         albums.extend(results['items'])
#
#     for album in albums:
#         print(album['name'])
#
#     return {"albums"}
#
# def get_album_image():
#     spotify = login()
#
#     artist= 'hugo tsr'
#     track= 'coma artificiel'
#
#     track_id = spotify.search(q='artist:' + artist + ' track:' + track, type='track')
#     # print(track_id)
#     # for x in track_id['tracks']:
#     print(track_id['tracks']['items'][0]['album']['images']) 
#     # GET album image
#     #print(track_id['tracks']['items'][0]['album']['images']) 





