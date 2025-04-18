import csv

class Music:
    #After the Class and the file_songs function, the code starts at the very bottom and calls the functions above it.
    #Decided to use f-string more since it's more applicable in the real-world and wanted to practice with it over break.
    #I would have liked to have learned how to call the file just once and use the data from that single call in the updated_file_rating function.
    #Also, I only have one try and except condition....I'll need to practice using those more in my code.
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
                f"and is {self.length} long.\n")

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

def exit_programme():
    print("Okay, thank you! Hope to see you again.\n")

#decided to re-read the file since we are only changing one data point
def update_file_rating(filename, matched_song, new_rating):
    updated_rows = []
    song_found = False
    with open(filename, 'r', encoding = 'utf-8') as file: 
        reader = csv.reader(file, quotechar = "'", skipinitialspace = True)
        for row in reader: 
            if len(row) >= 4:
                artist = row[0].strip()
                song_title = row[1].strip()
                if artist.casefold() == matched_song.artist.casefold() and song_title.casefold() == matched_song.song_title.casefold():
                   song_found = True
                try:
                       old_rating = int(row[4])
                       new_average = round((old_rating + new_rating) /2, 2)
                       row[4] = str(new_average)
                except (IndexError, ValueError):
                       if len(row) < 5: 
                           row.append(str(new_rating))
                       else: 
                           row[4] = str(new_rating)
                matched_song.average_rating = new_average if 'new_average' in locals() else new_rating
            updated_rows.append(row)
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, quotechar="'")
        writer.writerows(updated_rows)        

import math
def user_rating(song_list, matched_song):
    while True: 
        ask_rating = input("Would you like to rate this song? (y/n): ")
        if ask_rating == "y":
            while True:
                user_rating = input("Please enter a rating between 1 and 5, with 5 being amazing: ").strip().casefold()
                if user_rating in {"1", "2", "3", "4", "5"}:
                    new_user_rating = int(user_rating)
                    update_file_rating("music_data.txt", matched_song, new_user_rating)
                    print(f"Thanks! The new average rating for '{matched_song.song_title}' is now {matched_song.average_rating:.2f}.\n")
                    while True:
                        from_beginning = input("Would you like to start from the beginning? (y/n): ").strip().casefold()
                        if from_beginning == "y":
                            return start_searching(song_list)
                        elif from_beginning == "n":
                            return exit_programme()
                        else:
                            print("Sorry, please type either 'y' or 'n'.\n")
                else: 
                    print("\nSorry, I didn't catch that; can you try again?")
                    continue
        elif ask_rating == "n":
            while True:
                start_again = input("Okay, thank you. Please let me know what you'd like to do next (restart/end): ").strip().casefold()
                if start_again == "restart":
                    return start_searching(song_list)
                elif start_again == "end":
                    return exit_programme()
                else: 
                    print("Sorry, I didn't catch that. Please try again and type either 'restart' or 'end'.\n")
                    continue
        else:
            print("\nSorry I didn't catch that. Please type a whole number between 1 and 5.")
            continue

def play_song(song_list, matched_song):
    while True: 
        follow_up = input(f"Would you like to play <<{matched_song.song_title}>> by <<{matched_song.artist}>>? (y/n): ").strip().casefold()
        if follow_up == "y":
            print(f"{matched_song.song_title} by {matched_song.artist} is now playing...", end = '', flush = True)
            for _ in range(5):
                time.sleep(1)
                print(".", end = '', flush = True)
            print(f"\n{matched_song.song_title} has now finished playing.\n")
            return user_rating(song_list, matched_song)
        elif follow_up == "n":
            while True:
                start_over = input("Okay, I understand you don't want to play the song. Let me know what to do next (artists/songs/end): ")
                if start_over == "artists":
                    return artist_songs(song_list)
                elif start_over == "songs":
                    return search_songs(song_list)
                elif start_over == "end":
                    return exit_programme()
                else:
                    print("Sorry, I didn't catch that. Please type 'artist', 'song', or 'end'.\n")
                    continue
        else:         
            print("Unfortunately that is not playable. Please check your spelling as well and try again.\n")
            continue

#didn't have "time" (pun-intended) to figure out how to get the file to play the song for the full length of the seconds
import time
def search_songs(song_list):
    while True:
        user_song = input("Please enter a song title: ").strip().casefold()
        if not user_song:
            print("No song title entered. Please try again. \n")
            continue
        matched_song = next(
            (song for song in song_list if song.song_title.strip().casefold() == user_song.strip().casefold()),
            None
        )
        if matched_song:
            print(f"\n {matched_song.display_song()}")
            return play_song(song_list, matched_song)     
        else:
            print("Sorry that isn't a streamable song. Please check your spelling and try again.\n")
            continue

def artist_songs(song_list):    
    while True: 
        artist_name = input("Please enter an artist's name: ")
        if not artist_name: 
            print("No artist name entered.\n")
            continue
        matches = [song.song_title for song in song_list if song.artist.strip().casefold() == artist_name.strip().casefold()]
        if matches: 
            print(f"Songs by {artist_name}:\n" + "\n".join(matches) + "\n")
        else:
            print("Unfortunately, that artist is not streamable. Please check your spelling and try again.\n")
            continue
        while True:    
            follow_up = input("Would you like to search a specific song? (y/n):").strip().casefold()
            if follow_up == "y":
                return search_songs(song_list)
            elif follow_up == "n": 
                print("Thank you for using this programme and hope to see you again soon.\n")
                return start_searching(song_list)
            else:
                print("Sorry, I didn't catch that. Please type 'y' or 'n'.\n")
                continue

def start_searching(song_list):
    while True: 
        user_decision = input("Which would you like to search for? (artists/songs): ").strip().casefold()
        if user_decision == "artists":
            return artist_songs(song_list)
        if user_decision == "songs":
            return search_songs(song_list)
        else: 
            print("Unfortunately I didn't quite catch that. Please type either 'artists' or 'songs' and don't forget the 's' at the end of each word.\n")
            continue

songs = file_songs("music_data.txt")
start_searching(songs)