import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# List of Excel file paths (representing each "slice" of the cylinder at different depths)
excel_files = ['excel1.xlsx', 'excel2.xlsx', 'excel3.xlsx', 'excel4.xlsx']  # Add more files if needed

# Prepare arrays to store angle, distance, and depth data for the grid
angles_list = []
distances_list = []
depth_list = []

# Loop through each Excel file and extract the data
for depth, file in enumerate(excel_files):
    df = pd.read_excel(file)
    angles = df['Angle'].values
    distances = df['Distance'].values

    # Convert angles to radians for polar coordinates
    angles_in_radians = np.deg2rad(angles)

    # Store the data
    angles_list.append(angles_in_radians)
    distances_list.append(distances)
    depth_list.append(np.full_like(angles_in_radians, depth))  # Assign each sheet a depth (z-axis)

# Stack data to create a grid-like structure
angles_array = np.array(angles_list)
distances_array = np.array(distances_list)
depth_array = np.array(depth_list)

# Convert polar coordinates to cartesian for 3D plotting
X = distances_array * np.cos(angles_array)  # x-coordinates
Y = distances_array * np.sin(angles_array)  # y-coordinates
Z = depth_array  # z-coordinates (depth)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot only points using scatter
ax.scatter(X, Y, Z, c=Z, cmap='viridis', marker='o')

# Labels and title
ax.set_xlabel('X (cm)')
ax.set_ylabel('Y (cm)')
ax.set_zlabel('Depth (Layers)')
ax.set_title('3D Plot of Pipe ')

plt.show()
