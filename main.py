import argparse
import numpy as np
import utils as ut
import matplotlib.pyplot as plt
import cv2
import fast_fourier_transform as fft

parser = argparse.ArgumentParser(description="Beats per minute monitor using FFT by analyzing a video")
parser.add_argument("video", help="Video to analyze", type=str)
parser.add_argument("--size", "-s", help="Size of observed window. It is a square in the center of the screen.",
        type=int, default=30)
parser.add_argument("--npfft",help="Use numpy's fft method if True, use custom method if False",type=bool,default=True)
parser.add_argument("--filter", help="Filter the frecuencies between 50 and 130 bpm.", type=bool, default=False)

args = parser.parse_args()

cap = cv2.VideoCapture(args.video)
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
length = int(2 ** np.floor(np.log2(length)))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

size = args.size
upperLeftCornerX = width // 2 - size // 2
upperLeftCornerY = height // 2 - size // 2
lowerRightCornerX = width // 2 + size // 2
lowerRightCornerY = height// 2 + size // 2

r, g, b = ut.load_frames(cap,upperLeftCornerX,upperLeftCornerY,lowerRightCornerX,lowerRightCornerY,length)
cap.release()
cv2.destroyAllWindows()

n = length
f = np.linspace(-n/2,n/2-1,n)*fps/n
r = r[0,0:n]-np.mean(r[0,0:n])
g = g[0,0:n]-np.mean(g[0,0:n])
b = b[0,0:n]-np.mean(b[0,0:n])

fft_method = None
if args.npfft:
    fft_method = np.fft.fft
else:
    fft_method = fft.FFT_R

R = np.abs(np.fft.fftshift(fft_method(r)))**2
G = np.abs(np.fft.fftshift(fft_method(g)))**2
B = np.abs(np.fft.fftshift(fft_method(b)))**2
if args.filter:
    R,G,B = fft.band_pass_filter(R, G, B, f)

plt.subplot(2,1,1)
plt.plot(60*f,R, 'red')
plt.plot(60*f,G, 'green')
plt.plot(60*f,B, 'blue')
plt.xlim(0,200)
plt.xlabel("frecuencia [1/minuto]")

title = args.video.split("/")[-1].split(".")[0]
filename = ut.filename_builder(title, fps, len(r), args.size, args.filter)
plt.title(title)

plt.subplot(2,1,2)
plt.plot(np.arange(length),r, 'red')
plt.plot(np.arange(length),g, 'green')
plt.plot(np.arange(length),b, 'blue')
plt.xlabel("valor r g b")
plt.tight_layout()
ut.write_csv(filename, r, g, b, R, G, B)
plt.savefig("{}.png".format(filename))
#plt.show()
print("Frecuencia cardíaca: ", abs(f[np.argmax(R)])*60, " pulsaciones por minuto en R")
print("Frecuencia cardíaca: ", abs(f[np.argmax(G)])*60, " pulsaciones por minuto en G")
print("Frecuencia cardíaca: ", abs(f[np.argmax(B)])*60, " pulsaciones por minuto en B")

