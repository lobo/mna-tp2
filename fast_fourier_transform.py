import numpy as np

def FFT_SHIFT(x):
    n = len(x)
    return np.concatenate((x[n//2:n], x[0:n//2]), axis=0)

# FFT Implemented as described here:
# https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/
def FFT_R(x):
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    splitN = int(N/2)

    if np.log2(N) % 1 > 0:
        raise ValueError('values count must be a power of 2, "{}" given.'.format(N))
    if N < 2:
       return x
    else:
        X_even_values = FFT_R(x[::2])
        X_odd_values = FFT_R(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even_values + factor[:splitN] * X_odd_values,
                               X_even_values + factor[splitN:] * X_odd_values])


def band_pass_filter(R,G,B, f):
    BAND_PASS_LOWER_BOUND = 50
    BAND_PASS_UPPER_BOUND = 130
    for i in range(len(R)):
        if f[i]*60 < BAND_PASS_LOWER_BOUND  or f[i] * 60 > BAND_PASS_UPPER_BOUND:
            R[i] = 0
            G[i] = 0
            B[i] = 0

    return R, G, B


