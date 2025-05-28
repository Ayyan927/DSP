# FFT Frequency Analyzer - Frequency Domain Analysis
import numpy as np
import matplotlib.pyplot as plt

def analyze_frequencies(signal, sample_rate):
    N = len(signal)
    fft_result = np.fft.fft(signal)
    fft_freqs = np.fft.fftfreq(N, 1/sample_rate)
    magnitude = np.abs(fft_result) / N 
    half_N = N // 2
    plt.plot(fft_freqs[:half_N], magnitude[:half_N])
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()
sample_rate = 500
t = np.linspace(0, 1, sample_rate, endpoint=False)
signal = np.sin(2*np.pi*10*t) + 0.5*np.sin(2*np.pi*40*t) + 0.3*np.random.randn(sample_rate)

analyze_frequencies(signal, sample_rate)