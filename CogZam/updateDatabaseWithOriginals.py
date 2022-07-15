from CogZam import store_fingerprint, store_song, peak_extract, getFingerprints
from CogZam.recordingtoarray import getFile
import pickle
import numpy as np
import os

# assign directory
directory = '../songs/Original'

# iterate over files in
# that directory
fileList = []

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        fileList.append((f, filename))

massiveList = []
songDB = {}
fpDB = {}

print(fileList)

songID=0

for fileInfo in fileList:
    print(fileInfo[1])

    samples = getFile(fileInfo[0])
    title, artist = fileInfo[1][:-4].split(" - ")

    peaks = peak_extract(samples[0], samples[1])
    fingerprints = getFingerprints(peaks)

    store_fingerprint(fingerprints, songID, songDB, fpDB)
    store_song(songDB, title, artist, songID)

    songID+=1
