def find_song_name(song_id, song_database):
    for key in song_database.keys():
        if key == song_id:
            return song_database[key]

def tally_results(query, min_tally, song_database):
    tallies = Counter(query).most_common()
    highest_tally = tallies[0][1]
    id_w_highest_tally = tallies[0][0][0]
    if highest_tally >= min_tally:
        match = find_song_name(id_w_highest_tally, song_database)
        return f"The song is {match[0]} by {match[1]}."
    else:
        return "No match found."