class Music:
    def __init__(self, artist, song_title, length, genre, average_rating):
        self.artist = artist
        self.song_title = song_title
        self.length = length
        self.genre = genre
        try: 
            self.average_rating = int(average_rating)
        except ValueError:
            self.average_rating = "N/A"

    def display_song(self):
        return (f"The song, '{self.song_title}' is streamable.\n" 
        f"The artist is {self.artist}.\n" 
        f"This song is considered {self.genre},\n" 
        f"rated at a {self.average_rating} out of 5,\n" 
        f"and is {self.length} long.")

def file_songs(filename):
    song_list = []
    with open(filename, 'r') as file: 
        for line in file: 
            parts = line.strip().split(',')
            if len(parts) == 5: 
                artist, song_title, length, genre, average_rating = parts
            elif len(parts) == 4:
                artist, song_title, length, genre = parts
                average_rating = "N/A"
            else: 
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

songs = file_songs("music_data.txt")
print(search_songs(songs))

