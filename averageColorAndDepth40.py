import sys
import numpy as np
import cv2
from facenet_pytorch import MTCNN
import torch
from PIL import Image


filename1color=sys.argv[1]
filename2color=sys.argv[2]
filename3color=sys.argv[3]
filename4color=sys.argv[4]
filename5color=sys.argv[5]
filename6color=sys.argv[6]
filename7color=sys.argv[7]

filename1depth=sys.argv[8]
filename2depth=sys.argv[9]
filename3depth=sys.argv[10]
filename4depth=sys.argv[11]
filename5depth=sys.argv[12]
filename6depth=sys.argv[13]
filename7depth=sys.argv[14]

im1color=cv2.imread(filename1color)
im2color=cv2.imread(filename2color)
im3color=cv2.imread(filename3color)
im4color=cv2.imread(filename4color)
im5color=cv2.imread(filename5color)
im6color=cv2.imread(filename6color)
im7color=cv2.imread(filename7color)



im1depth=cv2.imread(filename1depth)
im2depth=cv2.imread(filename2depth)
im3depth=cv2.imread(filename3depth)
im4depth=cv2.imread(filename4depth)
im5depth=cv2.imread(filename5depth)
im6depth=cv2.imread(filename6depth)
im7depth=cv2.imread(filename7depth)


filenamecolor=sys.argv[15]
filenamedepth=sys.argv[16]
imcolor=im4color
im1depth=cv2.cvtColor(np.asarray(im1depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im2depth=cv2.cvtColor(np.asarray(im2depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im3depth=cv2.cvtColor(np.asarray(im3depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im4depth=cv2.cvtColor(np.asarray(im4depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im5depth=cv2.cvtColor(np.asarray(im5depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im6depth=cv2.cvtColor(np.asarray(im6depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
im7depth=cv2.cvtColor(np.asarray(im7depth,dtype=np.uint8),cv2.COLOR_BGR2GRAY)
imdepthfull=np.zeros((512,512))
for i in range(2,511):
    for j in range(2,511):

        currentarray=np.zeros((3,3))

        if im1depth[i][j]==255 or im2depth[i][j]==255 or im3depth[i][j]==255 or im4depth[i][j]==255 or im5depth[i][j]==255 or im6depth[i][j]==255 or im7depth[i][j]==255:
            imcolor[i][j][:]=255
            imdepthfull[i][j]=255
        else:
            for k in range(-1,1):
                for l in range(-1,1):
                    currentarray[k+1][l+1]=np.mean([im1depth[i+k][j+l],im2depth[i+k][j+l],im3depth[i+k][j+l],im4depth[i+k][j+l],im5depth[i+k][j+l],im6depth[i+k][j+l],im7depth[i+k][j+l]])
            imdepthfull[i][j]=np.mean(currentarray)

                

imdepth=imdepthfull
print("im1depth shape",im1depth.shape)
print("imdepth shape",imdepth.shape)
print("imdepth",np.max(imdepth))
#imdepth *= (255.0/imdepth.max())

device = 'cpu'
print('Running on device: {}'.format(device))
mtcnn=MTCNN(image_size=512, margin=0, min_face_size=50,thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True, device=torch.device(device))
frame = Image.fromarray(imcolor)
boxes0, val0 = mtcnn.detect(frame)
if boxes0 is not None:
    box = boxes0[0]
    print(" box is ",box)
    x,y,w,h=box
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)

    crop_color=imcolor[y:y+h,x:x+w,:]
    crop_depth=imdepth[y:y+h,x:x+w]
    imcolor=cv2.resize(crop_color,(512,512),interpolation=cv2.INTER_AREA)
    imdepth=cv2.resize(crop_depth,(512,512),interpolation=cv2.INTER_AREA)
    cv2.imwrite(filenamecolor,imcolor)
    cv2.imwrite(filenamedepth,imdepth)
else:
    cv2.imwrite(filenamecolor,imcolor)
    cv2.imwrite(filenamedepth,imdepth)


