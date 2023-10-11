import open3d as o3d
import sys
import trimesh
import numpy as np
from sklearn.neighbors import KDTree

def display_inlier_outlier(filename,filename1,mesh,cloud, ind):
    inlier_cloud = cloud.select_down_sample(ind)
    outlier_cloud = cloud.select_down_sample(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    #outlier_cloud.paint_uniform_color([1, 0, 0])
    #inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    #print("inlier_cloud has colors",np.asarray(inlier_cloud.points))
    pointsPCD = np.asarray(inlier_cloud.points)
    colorsPCD = np.asarray(inlier_cloud.colors)
    verticesMesh = np.asarray(mesh.vertices)
    colorsMesh = np.asarray(mesh.vertex_colors)
    meshtree = KDTree(verticesMesh,leaf_size=2)

    for i in range(pointsPCD.shape[0]):
        currentPoint=np.expand_dims(pointsPCD[i],axis=0)
        nearest_dist, nearest_ind=meshtree.query(currentPoint, k=2)
        closestIndex=nearest_ind[0,0]
        #print("closestIndex",closestIndex)
        
        inlier_cloud.colors[i]=mesh.vertex_colors[closestIndex]
        #print("colorsMesh",colorsMesh[closestIndex])
        #print("inlier_cloud.colors[i]",inlier_cloud.colors[i])
    #inlier_cloud.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=1))
    inlier_cloud.estimate_normals()

    
    #inlier_cloud.compute_vertex_normals()
    mesh1, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(inlier_cloud, depth=9)
    pcd1 = mesh1.sample_points_poisson_disk(60000)
    mesh1, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd1, depth=9)
    print("mesh from poisson reconstruction",mesh1)
    o3d.io.write_triangle_mesh(filename1,mesh1,write_ascii=True)
    
    o3d.io.write_point_cloud(filename,inlier_cloud,write_ascii=True)


if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    mesh= o3d.io.read_triangle_mesh(sys.argv[1])
    pcd = o3d.io.read_point_cloud(sys.argv[1])
    print("pcd mesh has vertex_colors",mesh.has_vertex_colors())
    print("mesh.vertex_colors",pcd.colors)
    #o3d.visualization.draw_geometries([pcd])

    #print("Downsample the point cloud with a voxel of 0.02")
    #voxel_down_pcd = pcd.voxel_down_sample(voxel_size=0.02)
    #o3d.visualization.draw_geometries([voxel_down_pcd])

    #print("Every 5th points are selected")
    #uni_down_pcd = pcd.uniform_down_sample(every_k_points=5)
    #o3d.visualization.draw_geometries([uni_down_pcd])

    print("Statistical oulier removal")
    cl, ind = pcd.remove_statistical_outlier(nb_neighbors=20,std_ratio=2.0)
    display_inlier_outlier(sys.argv[2],sys.argv[3],mesh,pcd, ind)

    #print("Radius oulier removal")
    #cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)
    #display_inlier_outlier(voxel_down_pcd, ind)
