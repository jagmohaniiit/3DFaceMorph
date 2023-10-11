import glob
import os
import sys
import shutil

baseDirectoryPath="./"
outputDirectoryPath="./"
filenamesPly=glob.glob(baseDirectoryPath+"**/*_translatedScaled.ply",recursive=True)
for i in range(len(filenamesPly)):
    print("processing mesh ",i)
    currentFilename=filenamesPly[i]
    ppmFilename=currentFilename.replace(".ply",".ppm")
    depthTxtFilename=currentFilename.replace(".ply","depth.txt")
    modelFilename=currentFilename.replace(".ply","_model.txt")
    viewFilename=currentFilename.replace(".ply","_view.txt")
    projectionFilename=currentFilename.replace(".ply","_projection.txt")
    depthPngFilename=currentFilename.replace(".ply","depth.png")
    command="./mesh_view_screenshot "+ppmFilename+" "+depthTxtFilename+" "+modelFilename+" "+viewFilename+" "+projectionFilename+" "+currentFilename
    print(command)
    os.system(command)
    command="python genDepthData.py "+depthTxtFilename+" "+depthPngFilename
    print(command)
    os.system(command)


