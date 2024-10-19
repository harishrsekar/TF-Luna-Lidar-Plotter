import pandas as pd
import numpy as np

# Generate angles from 0 to 360 degrees
full_angles = np.arange(0, 361)  # Angles from 0 to 360 degrees

# Generate random distances with an average of 10 cm and small variability
np.random.seed(42)  # For reproducibility
irregular_distances = np.random.normal(loc=10, scale=1, size=len(full_angles))  # Normal distance around 10 cm

# Convert the distances to integers
irregular_distances = np.round(irregular_distances).astype(int)

# Introduce a spike in distance between 30 and 40 degrees
spike_start = 30
spike_end = 40
spike_value = np.random.normal(loc=15, scale=1, size=(spike_end - spike_start + 1))  # Spike around 15 cm
spike_value = np.round(spike_value).astype(int)  # Convert spike values to integers

irregular_distances[spike_start:spike_end + 1] = spike_value

# Create a DataFrame with the angles and distances
df = pd.DataFrame({
    'Angle': full_angles,
    'Distance': irregular_distances
})

# Write the DataFrame to an Excel file
output_file = 'excel4.xlsx'
df.to_excel(output_file, index=False)

print(f"Excel file '{output_file}' has been created with the generated data.")
