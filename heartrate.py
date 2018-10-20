# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import cv2
import fast_fourier_transform as fft

cap = cv2.VideoCapture('./given-data/2017-09-14 21.53.59.mp4')

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

upperLeftCornerX = 610
upperLeftCornerY = 330
lowerRightCornerX = 640
lowerRightCornerY = 360

r = np.zeros((1,length))
g = np.zeros((1,length))
b = np.zeros((1,length))

currentFrameNo = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        # Cambiar estas frames
        r[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,0])
        g[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,1])
        b[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,2])
    else:
        break
    currentFrameNo += 1


cap.release()
cv2.destroyAllWindows()

n = 1024
f = np.linspace(-n/2,n/2-1,n)*fps/n
print(f)
r = r[0,0:n]-np.mean(r[0,0:n])
g = g[0,0:n]-np.mean(g[0,0:n])
b = b[0,0:n]-np.mean(b[0,0:n])

R = np.abs(np.fft.fftshift(fft.FFT_R(r)))**2
G = np.abs(np.fft.fftshift(fft.FFT_R(g)))**2
B = np.abs(np.fft.fftshift(fft.FFT_R(b)))**2

plt.plot(60*f,R, 'red')
plt.xlim(0,200)

plt.plot(60*f,G, 'green')
plt.xlim(0,200)

plt.plot(60*f,B, 'blue')
plt.xlim(0,200)
plt.show()

print("Frecuencia cardíaca: ", abs(f[np.argmax(G)])*60, " pulsaciones por minuto")
