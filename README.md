# 3DFaceMorph
The repository provides sample code for the paper "3D Face Morphing Attacks: Generation, Vulnerability and Detection", accepted in IEEE TBIOM and available at Arxiv (https://arxiv.org/abs/2201.03454).
The code sample can be executed by running completeScript.sh on Ubuntu 18.04 with python3.6 and pymeshlab library.
The code proceeds in the following order.
1) The code sample first generates color and depth maps from point clouds of two individuals.
2) It then generates a color image and depth map of the morph.
3) The point cloud is generated for the face morphing image and depth.
4) A small manual cleanup step of the generated face morphing point cloud.
5) A hole-filled point cloud is generated, which could be cleaned further.
