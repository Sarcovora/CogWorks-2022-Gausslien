def query_database(fp_database, fi_fj_dt, clip_time):
    q_songs = []
    if fi_fj_dt in fp_database:
        for song_id, song_time in fp_database[fi_fj_dt]:
            offset = song_time - clip_time
            q_songs.append((song_id, offset))
        return q_songs
    else:
        return q_songs