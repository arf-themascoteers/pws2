import librosa
import soundfile
import matplotlib.pyplot as plt
import simpleaudio
import time
import collections
import numpy as np

waveform, sample_rate = librosa.load("amplified.wav")
#simpleaudio.play_buffer(waveform, sample_rate=sample_rate, bytes_per_sample=4, num_channels=1)
#time.sleep(3)

#waveform = librosa.effects.trim(waveform, top_db=10)[0]
#soundfile.write("amplified.wav", waveform, sample_rate)

plt.plot(waveform)
plt.show()

waveform1_deq = collections.deque(waveform)
waveform1_deq.rotate(10000)
waveform2 = np.array(waveform1_deq)



waveform_resuling = (waveform + waveform2)/2
plt.plot(waveform_resuling)
plt.show()

simpleaudio.play_buffer(waveform_resuling, sample_rate=sample_rate, bytes_per_sample=4, num_channels=1)
time.sleep(3)
