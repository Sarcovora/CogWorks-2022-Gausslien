import pickle
import numpy as np

"""
Saves the passed dictionary of fingerprints
The database can be switched if a different dictionary is passed
"""
def save_fp_database(fp_database: dict):
    with open("fingerprint_database.pkl", mode="wb") as opened_file:
        pickle.dump(fp_database, opened_file)

"""
Loads and returns the dictionary of fingerprints
"""
def load_fp_database():
    with open("fingerprint_database.pkl", mode="rb") as opened_file:
        return pickle.load(opened_file)

"""
Saves the passed dictionary of song samples
The database can be switched if a different dictionary is passed
"""
def save_song_database(song_database: dict):
    with open("song_database.pkl", mode="wb") as opened_file:
        pickle.dump(song_database, opened_file)

"""
Loads and returns the dictionary of song samples
"""
def load_song_database():
    with open("song_database.pkl", mode="rb") as opened_file:
        return pickle.load(opened_file)

"""
Adds a song to the song database using its ID
Also prevents duplicates in the database
"""
def store_song(song_db: dict, song_name: str, artist_name: str, ID: int):
    song_item = [song_name, artist_name]
    if song_item not in song_db.values():
        song_db[ID] = song_item
        save_song_database(song_db)

"""
Checks if the given song by the artist is in the song database
"""
def song_with_artist_exists(song_db: dict, song_name: str, artist_name: str):
    if [song_name, artist_name] in song_db.values():
        return True
    return False

"""
Gets the song ID using the song name and artist
Prerequisite: song with artist must exist or else nothing gets returned
"""
def get_song_ID(song_db: dict, song_name: str, artist_name: str):
    song_item = [song_name, artist_name]
    for key, value in song_db.items():
        if value == song_item:
            return key

"""
Deletes a song from both the song database and the fingerprint database
"""
def delete_from_both_databases(song_db: dict, fp_db: dict, song_name: str, artist_name: str):
    if song_with_artist_exists(song_db, song_name, artist_name):
        ID_val = get_song_ID(song_db, song_name, artist_name)
        del song_db[ID_val]
        for value in fp_db.values():
            for curr_item in value:
                if curr_item[0] == ID_val:
                    value.remove(curr_item)
        save_song_database(song_db)
        save_fp_database(fp_db)