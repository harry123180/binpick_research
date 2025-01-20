import trimesh
import numpy as np
import os

# 定義相對路徑
stl_path = "C:\\Users\\TSIC\Documents\\GitHub\\binpick_research\\Tee_Pipe_Fitting_v1.stl"
print(f"Loading STL file from: {stl_path}")

# 讀取 STL 文件
mesh = trimesh.load(stl_path)

# 提取頂點座標
vertices = mesh.vertices  # 頂點座標 (N x 3 的 NumPy 陣列)

# 提取面片的頂點索引
faces = mesh.faces  # 每個面片由三個頂點組成 (M x 3 的 NumPy 陣列)

# 保存頂點到 numpy 文件
np.save('vertices.npy', vertices)
print("Vertices saved to vertices.npy")

# 保存面片索引到 numpy 文件（可選）
np.save('faces.npy', faces)
print("Faces saved to faces.npy")
