
def make_album(artist, album, songs = "0"):    
    artist = {"Artist Name":artist, "Album":album, "Songs":songs}
    for key, value in artist.items():
        print(f"Added: {key} {value}")


quit = ""

while quit == "":
    band = input("add artist:")
    cd = input("add album:")
    track = input("add track count:")
    make_album(band, cd, track)
    quit = input("press q to quit or enter to add another band")
    if quit == "q":
        break


