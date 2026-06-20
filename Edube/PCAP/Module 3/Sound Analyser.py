import numpy as np

def analyze_stress(signal):

    signal = np.array(signal,dtype=float)

    rms = np.sqrt(np.mean(signal**2))

    level = rms*10000

    if level < 1:
        state = "Silent"

    elif level < 50:
        state = "Feeble Voice"

