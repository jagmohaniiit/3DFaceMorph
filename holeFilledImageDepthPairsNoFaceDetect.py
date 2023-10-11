import cv2
import os
import sys
import json
import sys
import numpy as np
import cv2
import sys
from facenet_pytorch import MTCNN
import torch
import numpy as np
import mmcv, cv2
from PIL import Image, ImageDraw
import glob
import os
import time
import dlib
#from deepface import DeepFace
#from deepface.commons import functions

#backends = ['opencv', 'ssd', 'dlib', 'mtcnn']


def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    # Perform the rotation
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated



#device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
device = 'cpu'
print('Running on device: {}'.format(device))






#mtcnn=MTCNN(image_size=512, margin=0, min_face_size=50,thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True, device=torch.device(device))
#frame = Image.fromarray(cv2.cvtColor(cv2.imread(sys.argv[1]), cv2.COLOR_BGR2RGB))
#boxes0, val0 = mtcnn.detect(frame)
#box = boxes0[0]
#print("boxes0 is ",boxes0)
#crop_img_color = frame.crop(box)
#crop_img_color.save(sys.argv[3])
color_frame = Image.fromarray(cv2.cvtColor(cv2.imread(sys.argv[1]),cv2.COLOR_BGR2RGB))
depth_frame = Image.fromarray(cv2.imread(sys.argv[2],0))
#crop_img_depth = depth_frame.crop(box)
#indices=np.where(depth_frame==1)
print("depth image data")
img_color_np=np.asarray(color_frame)
img_depth_np=np.asarray(depth_frame)
print(np.asarray(img_depth_np))
maskDepth=np.zeros(np.asarray(img_depth_np).shape,dtype=np.uint8)

for i in range(0,img_depth_np.shape[0]):
    for j in range(100,img_depth_np.shape[1]):

        if img_depth_np[i][j]==255:
            i0 = i
            j0 = j
            distCorner0=np.sqrt((i0*i0)+(j0*j0))
            i0 = i-512
            j0 = j
            distCorner1=np.sqrt((i0*i0)+(j0*j0))
            i0 = i-512
            j0 = j-512

            distCorner2=np.sqrt((i0*i0)+(j0*j0))
            i0 = i
            j0 = j-512


            distCorner3=np.sqrt((i0*i0)+(j0*j0))
            minCornerDistance=np.min(np.array([distCorner0,distCorner1,distCorner2,distCorner3]))
            i0 = i-256
            j0 = j-256
            centerDistance=np.sqrt((i0*i0)+(j0*j0))
            if centerDistance < minCornerDistance:
                maskDepth[i][j]=255

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
maskDepth = cv2.dilate(maskDepth, kernel)



print("maskDepth shape",maskDepth.shape)
#maskDepth[indices]=255
depth_frame_inpainted=cv2.inpaint(np.asarray(img_depth_np),maskDepth,7, cv2.INPAINT_TELEA)
color_frame_inpainted=cv2.inpaint(np.asarray(img_color_np),maskDepth,7, cv2.INPAINT_TELEA)
cv2.imwrite(sys.argv[4],cv2.resize(depth_frame_inpainted,(512,512),interpolation = cv2.INTER_AREA))
cv2.imwrite(sys.argv[3],cv2.cvtColor(cv2.resize(color_frame_inpainted,(512,512),interpolation=cv2.INTER_AREA),cv2.COLOR_RGB2BGR))
cv2.imwrite("mask.png",maskDepth)

#crop_img_depth.save(sys.argv[4])






#image_save = crop_img.resize((224,224), Image.BILINEAR)

#result=detector.detect_faces(img)
#print("result is ",result)
#x, y, width, height = result[0]['box']
#print("x,y, width, height",x,y,height,width)
#imgDepth = cv2.imread(sys.argv[2])


















