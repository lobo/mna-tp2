import numpy as np
import utils as ut
import matplotlib.pyplot as plt
import cv2
import fast_fourier_transform as fft
    
def collect(video, size=300, npfft=True, filter_signal=False, persist=True, verbose=True, time_start=0, time_finish=1):
    """ params:
    video: String with the filename of the video to analyze.
    size: Int with the size of the window to analyze. It is always centered.
    npfft: Boolean that determines whether we use our implementation of the fft or the one that comes with numpy
    filter_signal: Boolean that determines if we filter the signal between 50 and 130 bpm
    persist: Boolean that determines if we store the data of this run
    verbose: Boolean that determines if we print the current status of the script
    time_start: Double between [0,1) that determines the % of the length of the video from which to start. (time_start < time_finish)
    time_finish: Double between (0,1] that determines the % of the length of the video until we stop analyzing. (time_start < time_finish)
    """
    if time_start >= time_finish:
        raise 'Incorrect time_start and time_finish, time_start must be smaller than time_finish'

    if verbose:
        print('Opening video...')
    cap = cv2.VideoCapture(video)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    
    size = size
    upperLeftCornerX = width // 2 - size // 2
    upperLeftCornerY = height // 2 - size // 2
    lowerRightCornerX = width // 2 + size // 2
    lowerRightCornerY = height// 2 + size // 2
    
    if verbose:
        print('Loading frames..')
    r0, g0, b0 = ut.load_frames(cap,upperLeftCornerX,upperLeftCornerY,lowerRightCornerX,lowerRightCornerY,length, time_start, time_finish)
    cap.release()
    cv2.destroyAllWindows()
    
    n = int(2 ** np.floor(np.log2(r0.shape[1])))
    f = np.linspace(-n/2,n/2-1,n)*fps/n
    r0 = r0[0,0:n]
    g0 = g0[0,0:n]
    b0 = b0[0,0:n]
    r = r0-np.mean(r0)
    g = g0-np.mean(g0)
    b = b0-np.mean(b0)
    
    if verbose:
        print('Applying the Fourier Transform...')
    fft_method = None
    fft_shift_method = None
    if npfft:
        fft_method = np.fft.fft
        fft_shift_method = np.fft.fftshift
    else:
        fft_method = fft.FFT_R
        fft_shift_method = fft.FFT_SHIFT

    R = np.abs(fft_shift_method(fft_method(r)))**2
    G = np.abs(fft_shift_method(fft_method(g)))**2
    B = np.abs(fft_shift_method(fft_method(b)))**2

    if filter_signal:
        R,G,B = fft.band_pass_filter(R, G, B, f)
    
    title = video.split("/")[-1].split(".")[0]
    filename = ut.filename_builder(title, fps, len(r), size, filter_signal)
    
    if persist:
        if verbose:
            print('Storing data...')
        if not filter_signal:
            plt.subplot(2,1,1)
        plt.plot(60*f,R, 'red')
        plt.plot(60*f,G, 'green')
        plt.plot(60*f,B, 'blue')
        plt.xlim(0,200)
        if filter_signal:
            plt.axvline(x=50, linestyle="--")
            plt.axvline(x=130, linestyle="--")
        plt.xlabel("frecuencia [1/minuto]")
        plt.annotate("{} latidos por minuto".format(abs(round(f[np.argmax(R)]*60,1))), xy=(1, 0), xycoords='axes fraction', fontsize=10,xytext=(0, -20), textcoords='offset points',ha='right', va='top')
        plt.title(title)
        
        if not filter_signal:
            plt.subplot(2,1,2)
            plt.plot(np.arange(n),r0, 'red')
            plt.plot(np.arange(n),g0, 'green')
            plt.plot(np.arange(n),b0, 'blue')
            plt.xlabel("valor r g b")
            plt.tight_layout()
    
        ut.write_csv(filename, r, g, b, R, G, B)
        plt.savefig("{}.png".format(filename))
        #plt.clf()


    if verbose:
        print("Frecuencia cardíaca: ", abs(f[np.argmax(R)])*60, " pulsaciones por minuto en R")
        print("Frecuencia cardíaca: ", abs(f[np.argmax(G)])*60, " pulsaciones por minuto en G")
        print("Frecuencia cardíaca: ", abs(f[np.argmax(B)])*60, " pulsaciones por minuto en B")
    return abs(round(f[np.argmax(R)]*60,1))

    
