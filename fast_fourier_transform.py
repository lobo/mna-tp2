import numpy as np

# FFT Implemented as described here:
# https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
def FFT_R(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    splitN = int(N/2)
    
    if np.log2(N) % 1 > 0:
        raise ValueError('values count must be a power of 2, "{}" given.'.format(N))
    elif N < 2:
        return x
    else:
        X_even_values = FFT_R(x[::2])
        X_odd_values = FFT_R(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even_values + factor[:splitN] * X_odd_values,
                               X_even_values + factor[splitN:] * X_odd_values])

