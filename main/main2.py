import csv

class Music:
    def __init__(self, artist, song_title, length, genre, average_rating):
        self.artist = artist
        self.song_title = song_title
        self.length = self.clean_length(length)
        self.genre = genre
        try: 
            self.average_rating = int(average_rating)
        except ValueError:
            self.average_rating = "N/A"

    def clean_length(self, length):
        return length.replace("seconds", "").strip() + " seconds"

    def display_song(self):
        return (f"The song, '{self.song_title}' is streamable.\n" 
                f"The artist is {self.artist}.\n" 
                f"This song is considered {self.genre},\n" 
                f"rated at a {self.average_rating} out of 5,\n" 
                f"and is {self.length} long.")

def file_songs(filename):
    song_list = []
    with open(filename, 'r', encoding='utf-8') as file: 
        reader = csv.reader(file, quotechar="'", skipinitialspace = True)
        for row in reader:
            if len(row) < 4:
                print(f"Skipping incomplete row: {row}")
                continue
            elif len(row) == 4:
                artist, song_title, length, genre = row
                average_rating = "N/A"
            elif len(row) == 5:
                artist, song_title, length, genre, average_rating = row
            else:
                print(f"Skipping malformed row: {row}")
                continue
            song = Music(artist, song_title, length, genre, average_rating)
            song_list.append(song)
    return song_list

def search_songs(song_list):
    while True:
        user_song = input("Please enter a song title: ")
        if not user_song:
            return "No song title entered."
        for song in song_list:
            if song.song_title.strip().lower() == user_song.lower():
                return song.display_song()
        print("Unfortunately, that song is not streamable.")

def artist_songs(song_list):
    while True: 
        artist_name = input("Please enter an artist's name: ")
        if not artist_name: 
            return "No artist name entered."
        matches = [song.song_title for song in song_list if song.artist.strip().lower() == artist_name.lower()]
        if matches: 
            return f"Songs by {artist_name}:\n" + "\n".join(matches)
        else:
            print("Unfortunately, that artist is not streamable.")

songs = file_songs("music_data.txt")
print(search_songs(songs))
print(artist_songs(songs))
