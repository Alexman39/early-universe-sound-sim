import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Simulation Parameters
duration = 5.0 # seconds
sampling_rate = 44100 # Hz (Cd-quality audio)
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Simulate a mix of harmonic waves representing early universe sounds
frequencies = [55, 110, 165, 220, 275, 330] # Like acoustic oscillations
amplitudes = [1.0, 0.7, 0.5, 0.3, 0.2, 0.1]

# Generate waveform
waveform = sum(a * np.sin(2 * np.pi * f * t) for f, a in zip(frequencies, amplitudes))

# Normalize the waveform to -1 to 1
waveform /= np.max(np.abs(waveform))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], waveform[:1000]) # Zoom in on the first ~0.02s
plt.title("Simulated Early-Universe Sound Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Play the sound
print("Playing the sound the of the early universe...")
sd.play(waveform, samplerate=sampling_rate)
sd.wait()
