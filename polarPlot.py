import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# File path for your Excel file
file_path = r"excel1.xlsx"

# Reading the Excel file
df = pd.read_excel(file_path)

# Extracting angles and distances
angles = df['Angle'].values  # Assuming the column name is 'Angle (Â°)'
distances = df['Distance'].values  # Assuming the column name is 'Distance (cm)'

# Convert angles to radians (for polar plot)
angles = np.deg2rad(angles)

# Plotting the radar-like graph
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location('N')  # North at the top
ax.set_theta_direction(-1)  # Clockwise direction

ax.plot(angles, distances)
ax.fill(angles, distances, alpha=0.3)  # Fill the area under the curve
ax.set_title("Lidar Output (Angle vs Distance)")

plt.show()
