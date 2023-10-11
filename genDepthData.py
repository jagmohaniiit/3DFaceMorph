import cv2
import numpy as np
import sys
depthData=np.genfromtxt(sys.argv[1],delimiter=' ').reshape(512,512)
depthDatauint16=(depthData*255).astype(np.uint8)
depthData8bit=depthDatauint16
cv2.imwrite(sys.argv[2],(depthData8bit).astype(np.uint8))
