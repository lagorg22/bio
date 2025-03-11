# Import necessary libraries
import pandas as pd
import numpy as np

# Load the data
# Replace 'your_data.csv' with the actual file path when running
data = pd.read_csv('data.csv')

# Extract ellipse parameters from the last row
ellipse = data.iloc[-1]
center_x = ellipse['X']          # X-coordinate of the ellipse center
center_y = ellipse['Y']          # Y-coordinate of the ellipse center
a = ellipse['Feret'] / 2         # Semi-major axis (Feret's diameter / 2)
b = ellipse['MinFeret'] / 2      # Semi-minor axis (MinFeret's diameter / 2)
angle = ellipse['FeretAngle']    # Orientation angle of the ellipse in degrees

# Extract centromere coordinates (all rows except the last)
centromeres = data.iloc[:-1]
x_coords = centromeres['X'].to_numpy()
y_coords = centromeres['Y'].to_numpy()

# Calculate distances from centromeres to the center
distances_to_center = np.sqrt((x_coords - center_x)**2 + (y_coords - center_y)**2)

# Calculate distances from the center to the ellipse edge along each centromere's direction
# Translate points relative to the center
x_trans = x_coords - center_x
y_trans = y_coords - center_y

# Rotate points to align the ellipse with the coordinate axes
angle_rad = np.deg2rad(angle)
cos_angle = np.cos(-angle_rad)
sin_angle = np.sin(-angle_rad)
x_unrot = x_trans * cos_angle - y_trans * sin_angle
y_unrot = x_trans * sin_angle + y_trans * cos_angle

# Calculate the angle (theta) for each point in the unrotated system
theta = np.arctan2(y_unrot, x_unrot)

# Calculate the distance from the center to the ellipse edge at each theta
distances_to_edge = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)

# Calculate the distance from each centromere to the periphery
distances_to_periphery = distances_to_edge - distances_to_center

# Add results to the original dataframe for the centromere rows
data['Distance_to_Center'] = np.nan
data['Center_to_Edge_Distance'] = np.nan
data['Distance_to_Periphery'] = np.nan
data.loc[data.index[:-1], 'Distance_to_Center'] = distances_to_center
data.loc[data.index[:-1], 'Center_to_Edge_Distance'] = distances_to_edge
data.loc[data.index[:-1], 'Distance_to_Periphery'] = distances_to_periphery

# Display the results for the centromeres
print("Centromere Distances from the Nuclear Periphery:")
display = data.iloc[:-1][['X', 'Y', 'Distance_to_Center', 'Center_to_Edge_Distance', 'Distance_to_Periphery']]
print(display)

# Save the updated dataframe to a new CSV file
data.to_csv('centromere_distances.csv', index=False)
print("\nResults saved to 'centromere_distances.csv'")
