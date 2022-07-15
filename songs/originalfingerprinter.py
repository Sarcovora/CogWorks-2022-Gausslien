import pickle

with open("songPaths.txt") as f:
    fileList = f.read().split('\n')[:-1]

massiveList = []
    
for i in fileList:
    print(i)
    samples = getFile(i)

    peaks = peak_extract(samples[0], samples[1])
    fingerprints = getFingerprints(peaks)
    massiveList.append(fingerprints)

with open('pickledSongs.pkl','wb') as f:
    pickle.dump(massiveList,f)
