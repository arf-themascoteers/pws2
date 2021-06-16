import librosa
import soundfile
import matplotlib.pyplot as plt
import simpleaudio
import time
import collections
import numpy as np
import random

sample_rate = 22050
t = np.linspace(0,1000,30000)
sine1 = np.sin(t)
sine2 = np.sin(t/5)
# sine2 = np.sin(t/40)
# np.roll(sine2)
sine3 = (sine1 + sine2)/2
sine4 = sine3.copy()
sine4 = np.roll(sine4,1000)
sine5 = sine3 + sine4
plt.plot(t, sine5)
plt.show()
simpleaudio.play_buffer(sine5, sample_rate=sample_rate, bytes_per_sample=4, num_channels=1)
soundfile.write("modified.wav", sine5, sample_rate)

