from microphone import record_audio
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
import librosa

def micRecord(time=10):
    frames, rate = record_audio(time)
    return np.hstack([np.frombuffer(i, np.int16) for i in frames]), rate


def getFile(path):
    recorded_audio, sampling_rate = librosa.load(path, 
                                                 sr=44100, 
                                                 mono=True, 
                                                 offset=1.5, 
                                                 duration=20)
    return recorded_audio, sampling_rate

def userinput():
    while True:
        audioType = input("u for Upload, r for Record: ")
        if audioType == 'u':
            path = input("Enter path to file: ")
            samples, rate = getFile(path)
            break
        elif audioType == 'r':
            samples, rate = micRecord()
            break
        print("Invalid input. Try again.")
    print(rate)
    
    return samples, rate
