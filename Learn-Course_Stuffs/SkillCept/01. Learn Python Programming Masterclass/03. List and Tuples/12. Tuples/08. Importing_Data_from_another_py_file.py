from Albums import albums

SONGS_LIST_INDEX = 3

try:
    while True:
        print("Available Albums:")
        for index, (title, artist, year, songs) in enumerate(albums):
            print("{}. {}".format(index+1, title))
        print("0. Exit")
        album_choice = int(input("Select your desired album: "))

        if 1<= album_choice <= len(albums):
            song_list = albums[album_choice-1][SONGS_LIST_INDEX]
            for song in song_list:
                print(song)
            song_choice = int(input("Select song to play: "))
            if 1<= song_choice <= len(song_list):
                print("=" * 101)
                print("'{}' is playing... Listen and Enjoy...".format(song_list[song_choice-1]))
            print("=" * 101, "\n") 

        elif album_choice == 0:
            print("Successfully Exit")
            break
        else:
            print("Invalid ALBUM Choice....\nRun again")
            break

except:
    print("Wrong Input")