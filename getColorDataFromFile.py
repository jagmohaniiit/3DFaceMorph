import cv2
import numpy as np
import sys
import os
inputFilename=sys.argv[1]
if ".ppm" in inputFilename:
    command="convert "+inputFilename+" "+"./KeypointAlignment/colorImage.png"
    inputFilename="./KeypointAlignment/colorImage.png"
    os.system(command)


print(inputFilename)
inputImage=cv2.imread(inputFilename)
print("isshape",inputImage.shape)
imageData=cv2.cvtColor(cv2.imread(inputFilename),cv2.COLOR_BGR2RGB)
imwidth,imheight=imageData.shape[0:2]
if imwidth != 512 or imheight != 512:
    imageData=cv2.resize(imageData,(512,512),interpolation=cv2.INTER_AREA)


print("imageData",imageData)

np.savetxt("./KeypointAlignment/colorDataRed.txt",imageData[:,:,0],delimiter=' ',fmt='%d')
np.savetxt("./KeypointAlignment/colorDataGreen.txt",imageData[:,:,1],delimiter=' ',fmt='%d')
np.savetxt("./KeypointAlignment/colorDataBlue.txt",imageData[:,:,2],delimiter=' ',fmt='%d')

if os.path.exists("./KeypointAlignment/colorImage.png"):
    command="rm ./KeypointAlignment/colorImage.png"
    #os.system(command)
