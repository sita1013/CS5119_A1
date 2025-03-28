class Music:
    def __init__(self, artist, song_title, length, genre, average_rating):
        self.artist = artist
        self.song_title = song_title
        self.length = length
        self.genre = genre
        self.average_rating = average_rating

    def display_song(self):
        user_title = input("Please enter a song title: ")
        try:
            while user_title != self.song_title:
                print("Unfortunately, that song is not streamable.")
                user_title = input("Please try another song title: ")
        finally: 
            return f"The song, '{user_title}' is streamable.\n The artist is {self.artist}.\n This song is considered {self.genre},\n rated at a {self.average_rating} out of 5,\n and is {self.length} long."

    def file_songs(music_data.txt):
        song_list = []
        with open(music_data.txt, 'r') as file: 
            for line in file: 
                info = line.strip().split(',')
                if len(parts) == 5:
                    artist, song_title, length, genre, average_rating = parts
                    song = Music(artist, song_title, length, genre, average_rating)
                    song_list.append(song)
        return song_list

    



