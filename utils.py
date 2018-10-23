import numpy as np

def load_frames(cap,upperLeftCornerX,upperLeftCornerY,lowerRightCornerX,lowerRightCornerY,length):
    r = np.zeros((1,length))
    g = np.zeros((1,length))
    b = np.zeros((1,length))
    
    currentFrameNo = 0
    while(cap.isOpened() and currentFrameNo < length):
        ret, frame = cap.read()
        
        if ret == True:
            r[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,0])
            g[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,1])
            b[0,currentFrameNo] = np.mean(frame[upperLeftCornerX:lowerRightCornerX, upperLeftCornerY:lowerRightCornerY,2])
        else:
            break
        currentFrameNo += 1
    print(currentFrameNo)
    return [r, g, b]

