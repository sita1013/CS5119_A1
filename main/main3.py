import csv

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
    with open(filename, 'r', encoding='utf-8') as file: 
        music_file = csv.reader(file, quotechar="'", skipinitialspace = True)
        for row in music_file:
            if len(row) < 4:
                print(f"Issues with this information and skipping row: {row}")
                continue
            elif len(row) == 4:
                artist, song_title, length, genre = row
                average_rating = "N/A"
            elif len(row) == 5:
                artist, song_title, length, genre, average_rating = row
            else:
                print(f"Skipping row due to problems with the information: {row}")
                continue
            song = Music(artist, song_title, length, genre, average_rating)
            song_list.append(song)
    return song_list

import time
def search_songs(song_list):
    while True:
        user_song = input("Please enter a song title: ").strip().casefold()
        if not user_song:
            print("No song title entered. Please try again: ")
            continue
        matched_song = next(
            (song for song in song_list if song.song_title.strip().casefold() == user_song.strip().casefold()),
            None
        )
        if matched_song:
            print(matched_song.display_song())
            while True: 
                follow_up = input(f"Would you like to play <<{matched_song.song_title}>> by <<{matched_song.artist}>>? (y/n): ").strip().casefold()
                if follow_up == "y":
                    print(f"{matched_song.song_title} by {matched_song.artist} is now playing...", end = '', flush = True)
                    for _ in range(5): 
                        time.sleep(1)
                        print(".", end = '', flush = True)
                    print(f"\n{matched_song.song_title} has now finished playing.")
                    break
                elif follow_up == "n":
                    break
                else: 
                    print("Invalid input. Please try again.")
        else:         
            print("Unfortunately that is not playable.")            
            while True:
                start_again = input("Okay thank you. Please type next command (start/end): ").strip().casefold()
                if start_again == "start":
                    return start_searching(song_list)
                elif start_again == "end":
                    print("Okay thank you and hope to see you again soon.")
                else:
                    print("Invalid input. Please try again.")
            while True:
                start_over = input("Would you like to search for anything else? (y/n): ").strip().casefold()
                if start_over == "y": 
                    break
                elif start_over == "n": 
                    print("Thank you for using this programme and hope to see you again soon.")
                    return
                else: 
                    print("Sorry that's not a correct input.")

def artist_songs(song_list):    
    while True: 
        artist_name = input("Please enter an artist's name: ")
        if not artist_name: 
            print("No artist name entered.")
        matches = [song.song_title for song in song_list if song.artist.strip().casefold() == artist_name.casefold()]
        if matches: 
            print(f"Songs by {artist_name}:\n" + "\n".join(matches))
        while True:    
            follow_up = input("Would you like to search a specific song? (y/n):").casefold()
            if follow_up == "y":
                return search_songs(song_list)
            elif follow_up == "n": 
                print("Thank you for using this programme and hope to see you again soon.")
                return start_searching(song_list)
            else:
                print("Sorry that's not a correct input.")
        else:
            print("Unfortunately, that artist is not streamable.")

def start_searching(song_list):
    while True: 
        user_decision = input("Which would you like to search for? (artists/songs): ").lower()
        if user_decision == "artists":
            return artist_songs(song_list)
        if user_decision == "songs": 
            return search_songs(song_list)
        else: 
            print("Unfortunately I didn't quite catch that. Please try again.")

songs = file_songs("music_data.txt")
print(start_searching(songs))

