import random

def long_to_short(samples:np.array, length:int, fs = 44100) -> np.ndarray:
    """"
        Given a long song (60 seconds) returns a random shorten 10 second clip 
    
        Parameters
        ----------
        samples : numpy.ndarray
            takes samples from getFile(path)
        
        fs = 44100
            sampling rate in Hz
    
        Returns
        -------
        numpy.ndarray
            The value of the digital signal at the given times.
        
    """
    
    samples_in_length = int(fs*length)
    rand_num = random.randint(0,len(samples)-samples_in_length)
    return samples[rand_num:rand_num +samples_in_length]
