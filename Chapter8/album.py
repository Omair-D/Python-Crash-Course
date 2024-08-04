# Write function make_album() - build dictionary describing music album (title returning 2 pieces of info)
def make_album(artist, title):
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return album_dict



