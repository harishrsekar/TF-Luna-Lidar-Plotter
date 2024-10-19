import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

excel_files = ['excel1.xlsx', 'excel2.xlsx', 'excel3.xlsx', 'excel4.xlsx']

angles_list = []
distances_list = []
depth_list = []

for depth, file in enumerate(excel_files):
    df = pd.read_excel(file)
    angles = df['Angle'].values
    distances = df['Distance'].values
    angles_in_radians = np.deg2rad(angles)
    angles_list.append(angles_in_radians)
    distances_list.append(distances)
    depth_list.append(np.full_like(angles_in_radians, depth))

angles_array = np.array(angles_list)
distances_array = np.array(distances_list)
depth_array = np.array(depth_list)

X = distances_array * np.cos(angles_array)
Y = distances_array * np.sin(angles_array)
Z = depth_array

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X, Y, Z, c=Z, cmap='viridis', marker='o')

ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Depth (Layers)')
ax.set_title('3D Plot of Pipe')

plt.show()
