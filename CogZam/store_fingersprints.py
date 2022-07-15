def store_fingerprint(fanout, song_ID, song_database, fp_database):
    if song_ID in song_database:
        return "That song ID is already in use"
    for (fm, fn, dt), tm in fanout:
        fp_database[(fm, fn, dt)].append((song_ID, tm))
    with open("placeholder", mode="wb") as f:
        pickle.dump(fp_database, f)