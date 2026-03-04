import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
duration = 3  # seconds

print("Recording... Speak now!")

audio = sd.rec(int(duration * fs),
               samplerate=fs,
               channels=1,
               dtype='int16')   # <-- ADD THIS

sd.wait()

write("sample.wav", fs, audio)

print("Saved as sample.wav")