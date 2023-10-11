import pymeshlab
import sys
import glob
import os
import time
inputFolder="./"
outputFolder="./"

filenames=glob.glob(inputFolder+"**/*ascii.ply",recursive=True)
print(filenames)



for i in range(len(filenames)):
    print("i is ",i)
    starttime=time.time()
    inputfilename=filenames[i]
    outputfilename=inputfilename.replace("_ascii.ply","_ascii_averaged.ply")
    filebasename=os.path.basename(inputfilename)
    filenametemp=outputFolder+filebasename.replace("_ascii.ply","_cropRot40.ppm")
    filenameaveragecolortemp=filenametemp.replace(".ppm","averagecolor.ppm")
    #if os.path.exists(filenameaveragecolortemp):
    #    continue
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot40.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot40.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot40.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot40.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot40.txt")
    filenamemodel=filename3
    filenameview=filename4
    filenameprojection=filename5
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 40 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot40.ppm")
    filename8=filename2.replace("Rot40.txt","_cropRot40.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename14=filename7
    filename24=filename8
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot10.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot10.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot10.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot10.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot10.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 10 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot10.ppm")
    filename8=filename2.replace("Rot10.txt","_cropRot10.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename11=filename9
    filename21=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename11+" "+filename21
    os.system(command)
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot20.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot20.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot20.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot20.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot20.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 20 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot20.ppm")
    filename8=filename2.replace("Rot20.txt","_cropRot20.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename12=filename9
    filename22=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename12+" "+filename22
    os.system(command)
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot30.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot30.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot30.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot30.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot30.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 30 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot30.ppm")
    filename8=filename2.replace("Rot30.txt","_cropRot30.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename13=filename9
    filename23=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename13+" "+filename23
    os.system(command)
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot50.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot50.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot50.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot50.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot50.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 50 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot50.ppm")
    filename8=filename2.replace("Rot50.txt","_cropRot50.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename15=filename9
    filename25=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename15+" "+filename25
    os.system(command)
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot60.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot60.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot60.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot60.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot60.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 60 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot60.ppm")
    filename8=filename2.replace("Rot60.txt","_cropRot60.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename16=filename9
    filename26=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename16+" "+filename26
    os.system(command)
    filename1=outputFolder+filebasename.replace("_ascii.ply","Rot70.ppm")
    filename2=outputFolder+filebasename.replace("_ascii.ply","depthRot70.txt")
    filename3=outputFolder+filebasename.replace("_ascii.ply","_modelRot70.txt")
    filename4=outputFolder+filebasename.replace("_ascii.ply","_viewRot70.txt")
    filename5=outputFolder+filebasename.replace("_ascii.ply","_projectionRot70.txt")
    command="./mesh_view_screenshot_boundingspherescaled_rotations "+filename1+" "+filename2+" "+filename3+" "+filename4+" "+filename5+" 70 "+inputfilename
    os.system(command)
    filename6=filename2.replace(".txt",".png")
    command="python genDepthData.py "+filename2+" "+filename6
    os.system(command)
    filename7=outputFolder+filebasename.replace("_ascii.ply","_cropRot70.ppm")
    filename8=filename2.replace("Rot70.txt","_cropRot70.png")
    command="python holeFilledImageDepthPairsNoFaceDetect.py "+filename1+" "+filename6+" "+filename7+" "+filename8
    os.system(command)
    filename9=filename7.replace(".ppm","registered.ppm")
    filename10=filename8.replace(".png","registered.png")
    filename17=filename9
    filename27=filename10
    command="python registerFacesPair.py "+filename7+" "+filename14+" "+filename8+" "+filename24+" "+filename17+" "+filename27
    os.system(command)
    filenameaveragecolor=filename14.replace(".ppm","averagecolor.ppm")
    filenameaveragedepth=filename24.replace(".png","averagedepth.png")
    command="python averageColorAndDepth40.py "+filename11+" "+filename12+" "+filename13+" "+filename14+" "+filename15+" "+filename16+" "+filename17+" "+filename21+" "+filename22+" "+filename23+" "+filename24+" "+filename25+" "+filename26+" "+filename27+" "+filenameaveragecolor+" "+filenameaveragedepth
    os.system(command)
    command="./mesh_view_pointcloudfromcoloranddepth "+filenameaveragecolor+" "+filenameaveragedepth+" "+filenamemodel+" "+filenameview+" "+filenameprojection+" "+outputfilename
    os.system(command)
    elapsed=time.time()-starttime
    print("elapsed time is",elapsed)
