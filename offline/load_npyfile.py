import numpy as np
import vedo
import os

# 加載已保存的頂點和面片數據
vertices_path = 'vertices.npy'
faces_path = 'faces.npy'

if not os.path.exists(vertices_path) or not os.path.exists(faces_path):
    raise FileNotFoundError("Required .npy files not found. Please ensure 'vertices.npy' and 'faces.npy' exist.")

# 加載數據
vertices = np.load(vertices_path)
faces = np.load(faces_path)

# 創建 vedo.Mesh
mesh_viz = vedo.Mesh([vertices, faces])

# 設置繪圖參數
mesh_viz.c("lightblue").lw(0.1)  # 設置顏色和線寬

# 使用 vedo 繪製並允許互動
plotter = vedo.Plotter()
plotter.show(mesh_viz, "Numpy-based STL Viewer", axes=1, viewup="z", interactive=True)
