import numpy as np
import imageio
import sys
import cv2
print("sys.argv[1]",sys.argv[1])
imageData=imageio.imread(sys.argv[1])
print(np.min(np.min(imageData)))
print(imageData.shape)
imwidth,imheight=imageData.shape[0:2]
if imwidth != 512 or imheight != 512:
    imageData=cv2.resize(imageData,(512,512),interpolation=cv2.INTER_AREA)
np.savetxt("./KeypointAlignment/depthData.txt",imageData,delimiter=' ',fmt='%d')


