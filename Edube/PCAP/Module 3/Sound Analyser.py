import numpy as np

def analyze_stress(signal):

    signal = np.array(signal,dtype=float)

    rms = np.sqrt(np.mean(signal**2))

 