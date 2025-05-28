#Moving Average Filter- Time Domain Processing
import numpy as np
import matplotlib.pyplot as plt

def moving_average(signal, window_size):
    weights = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(signal, weights, mode='valid')
    return smoothed_signal

t = np.linspace(0, 1, 100)
clean_signal = np.sin(2 * np.pi * 5 * t)
noise = 0.5 * np.random.randn(100)
noisy_signal = clean_signal + noise
filtered_signal = moving_average(noisy_signal, window_size=5)
plt.plot(t, noisy_signal, label='Noisy Signal')
plt.plot(t[2:-2], filtered_signal, label='Filtered Signal', linewidth=2)
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Simple Moving Average Filter')
plt.grid(True)
plt.show()