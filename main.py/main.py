class Music:
  def __init__(self, artist, song_title, length, genre, average_rating):
    self.artist = artist
    self.song_title = song_title
    self.length = length
    self.genre = genre
    self.average_rating = average_rating

  def check_song(self):
    user_title = input("Please enter a song title: ")
    try: 
      while user_title != self.song_title:
        print("Unfortunately, that song is not streamable.")
        user_title = input("Please try another song title: ")
    finally: 
      return f"The song, '{user_title}' is streamable.\n The artist is {self.artist}.\n This song is considered {self.genre},\n rated at a {self.average_rating} out of 5,\n and is {self.length} long."
  
c1 = Music("Radiohead", "Creep", "238 seconds", "Alternative Rock", 4)
print(c1.check_song())


