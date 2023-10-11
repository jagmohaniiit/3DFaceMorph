import glob
import os
import cv2
import numpy as np
import dlib
import faceBlendCommon as fbc
import sys
import trimesh
predictor_path="shape_predictor_68_face_landmarks.dat"
faceDetector = dlib.get_frontal_face_detector()
landmarkDetector = dlib.shape_predictor(predictor_path)



def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result


def Dot(v0,v1):
    result=(v0[0]*v1[0])+(v0[1]*v1[1])+(v0[2]*v1[2])
    return result



def Barycentric(p,a,b,c):

    v0 = b - a
    v1 = c - a
    v2 = p - a
    d00 = Dot(v0, v0)
    d01 = Dot(v0, v1)
    d11 = Dot(v1, v1)
    d20 = Dot(v2, v0)
    d21 = Dot(v2, v1)
    denom = d00 * d11 - d01 * d01
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1.0 - v - w
    if u>=0 and u<=1.0 and v>=0.0 and v<=1.0 and w>=0.0 and w<=1.0:
        return True
    else:
        return False




def findNearest3DPoint(currentPoint,points3DArray,scale=256.0):
    minDistance = 1.0e10
    minIndex = -1
    currentPoint = np.array(currentPoint,dtype=np.float)
    points3DArray = np.array(points3DArray,dtype=np.float)
    currentX = (currentPoint[0]/scale)
    currentY = (currentPoint[1]/scale)


    for i in range(0,points3DArray.shape[0]):
        pointX = (points3DArray[i][0])
        pointY = (points3DArray[i][1])

        xdiff = (currentX-pointX)*(currentX-pointX)
        ydiff = (currentY-pointY)*(currentY-pointY)
        dist = np.sqrt(xdiff+ydiff)

        if minDistance > (dist):
            minDistance = (dist)
            minIndex = i


    return minIndex




def getAffineTransform_3D(inputPoints,outputPoints):
    l = len(inputPoints)
    B = np.vstack([np.transpose(inputPoints), np.ones(l)])
    if np.linalg.det(B)==0:
        return np.ones((3,3)),np.array([0,0,0])
    D = 1.0 / np.linalg.det(B)
    entry = lambda r,d: np.linalg.det(np.delete(np.vstack([r, B]), (d+1), axis=0))
    M = [[(-1)**i * D * entry(R, i) for i in range(l)] for R in np.transpose(outputPoints)]
    A, t = np.hsplit(np.array(M), [l-1])
    t = np.transpose(t)[0]
    #print("A shape",A.shape,"t shape",t.shape)
    return A,t



def generateMorphSinglePair(filenameColor1,filenameDepth1,filenameColor2,filenameDepth2,filenameMorphColor,filenameMorphDepth):
    if ".ppm" in filenameColor1:
        command="convert "+filenameColor1+" "+filenameColor1.replace(".ppm",".png")
        os.system(command)
        filenameColor1=filenameColor1.replace(".ppm",".png")

    if ".ppm" in filenameColor2:
        command="convert "+filenameColor2+" "+filenameColor2.replace(".ppm",".png")
        os.system(command)
        filenameColor2=filenameColor2.replace(".ppm",".png")
        
    print(filenameColor1)
    print(filenameColor2)
    inputColor1=cv2.imread(filenameColor1)
    inputDepth1=cv2.imread(filenameDepth1)
    points1=fbc.getLandmarks(faceDetector, landmarkDetector, inputColor1)
    inputColor2=cv2.imread(filenameColor2)
    inputDepth2=cv2.imread(filenameDepth2)
    points2=fbc.getLandmarks(faceDetector, landmarkDetector, inputColor2)
    print("points1 length",len(points1))
    print("points2 length",len(points2))

    h=640
    w=640





    
    
  
    
     
    if len(points1) >= 68 and len(points2) >= 68:
        inputColor1 = np.float32(inputColor1)/255.0
        inputColor2 = np.float32(inputColor2)/255.0
        points1 = np.array(points1)
        points2 = np.array(points2)
        inputDepth1 = np.float32(inputDepth1)/255.0
        inputDepth2 = np.float32(inputDepth2)/255.0
        imCol1,imDepth1=fbc.normalizeImagesAndLandmarks((h,w), inputColor1, inputDepth1,points1)
        imCol2,imDepth2=fbc.normalizeImagesAndLandmarks((h,w), inputColor2, inputDepth2,points2)
        pointsAvg = (points1 + points2)/2.0
        # 8 Boundary points for Delaunay Triangulation
        boundaryPoints = fbc.getEightBoundaryPoints(h, w)
        points1 = np.concatenate((points1, boundaryPoints), axis=0)
        points2 = np.concatenate((points2, boundaryPoints), axis=0)
        pointsAvg = np.concatenate((pointsAvg, boundaryPoints), axis=0)
        # Calculate Delaunay triangulation
        rect = (0, 0, w, h)
        dt = fbc.calculateDelaunayTriangles(rect, pointsAvg)

        print("dt is",dt)
        
        alpha = 0.5
        pointsMorph = (1 - alpha) * points1 + alpha * points2
        imOut1 = fbc.warpImage(inputColor1, points1, pointsMorph.tolist(), dt)
        imOut2 = fbc.warpImage(inputColor2, points2, pointsMorph.tolist(), dt)
        imMorph = (1 - alpha) * imOut1 + alpha * imOut2
        imDepthOut1 = fbc.warpImage(inputDepth1, points1, pointsMorph.tolist(), dt)
        imDepthOut2 = fbc.warpImage(inputDepth2, points2, pointsMorph.tolist(), dt)
        imDepth = (1 - alpha) * imDepthOut1 + alpha * imDepthOut2
        outputFilename=filenameMorphColor
        print("outputFilename is",outputFilename)
        cv2.imwrite(filenameMorphColor,np.round(imMorph*255).astype(np.uint8))
        outputFilename=filenameMorphDepth
        imDepthOut=imDepth[:,:,0]
        print("shape imDepth",imDepthOut.shape)
        cv2.imwrite(filenameMorphDepth,np.round(imDepthOut*255).astype(np.uint8))
       


filenameColor1=sys.argv[1]
filenameDepth1=sys.argv[2]
filenameColor2=sys.argv[3]
filenameDepth2=sys.argv[4]
filenameMorphColor=sys.argv[5]
filenameMorphDepth=sys.argv[6]
generateMorphSinglePair(filenameColor1,filenameDepth1,filenameColor2,filenameDepth2,filenameMorphColor,filenameMorphDepth)

