def make_album(artist, album, number=None):
    """builds a dictionary describing a music album. """
    music_catalogue = {}
    music_catalogue['artist'] = artist
    music_catalogue['album'] = album
    if number:
        music_catalogue['number'] = number
    return music_catalogue

active = True
while active:
    print("Let's add your favorite album to a catalogue. Enter 'q' to exit. ")
    artist_ = input("Enter artist's name. ")
    if artist_ == 'q':
        break
    album_ = input("Enter album name. ")
    if album_ == 'q':
        break
    number_ = input("Enter number of songs in the album. ")
    if number_ == 'q':
        break
    print(make_album(artist_, album_, number_))