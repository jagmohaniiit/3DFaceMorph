rm *.ppm *.png *.txt
python scriptGenerateColorDepth.py
python generateMorphsSingleImagePairwithDepth.py AnkurShukla005_translatedScaled.ppm AnkurShukla005_translatedScaleddepth.png Raghu005_translatedScaled.ppm Raghu005_translatedScaleddepth.png AnkurShukla005_Raghu005_translatedScaled.ppm AnkurShukla005_Raghu005_translatedScaleddepth.png
./mesh_view_pointcloudfromcoloranddepth  AnkurShukla005_Raghu005_translatedScaled.ppm AnkurShukla005_Raghu005_translatedScaleddepth.png Raghu005_translatedScaled_model.txt Raghu005_translatedScaled_view.txt Raghu005_translatedScaled_projection.txt AnkurShukla005_Raghu005_translatedScaled.ply
python cleanOpen3dPointCloud.py AnkurShukla005_Raghu005_translatedScaled.ply AnkurShukla005_Raghu005_translatedScaled_cleaned.ply
#Manual Cleaning Step and Saving as Ascii Ply
python generateHoleFilledMeshes.py


