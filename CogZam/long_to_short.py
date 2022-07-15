def long_to_short(samples:np.array, length:int, num_of_clips = 10, fs = 44100) -> []:
    """"
        Parameters
        ----------
        samples : numpy.ndarray
            takes samples from getFile(path)
        
        fs = 44100
            sampling rate 
            
        num_of_clips = 10
            generates a default of 10 random clips
    
        Returns
        -------
        []
            A list of random clips with the value of the digital signal at the given times.
        
    """
    clips = []
    
    for i in range(num_of_clips):
        samples_in_length = int(fs*length)
        rand_num = random.randint(0,len(samples)-samples_in_length)
        clips.append(samples[rand_num:rand_num +samples_in_length])
    
    
    return clips
