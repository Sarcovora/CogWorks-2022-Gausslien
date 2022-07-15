from CogZam import store_fingerprint, store_song, getFile, load_fp_database, load_song_database, query_database, userinput, getFingerprints, peak_extract, tally_results
import pickle
import numpy as np

fp_database = load_fp_database()
song_database = load_song_database()

samples, sample_rate = userinput()

peaks = peak_extract(samples, sample_rate)
fingerprints = getFingerprints(peaks)

matches = {}
q_songs = []

for f in fingerprints:
	q_songs.extend(query_database(fp_database, f[0], f[1])) # [(songid, offset), (songid, offset), ...]


print((tally_results(tuple(q_songs), min_tally=5, song_database=song_database))) # change min_tally later
