import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import math

# Read CSV file
data = pd.read_csv('data.csv')

# Last row contains the nucleus ellipse parameters
nucleus = data.iloc[-1]
n_X = nucleus['X']
n_Y = nucleus['Y']
n_DiameterMax = nucleus['Feret']  # Major axis
n_DiameterMin = nucleus['MinFeret']  # Minor axis
n_RotAngle = nucleus['FeretAngle']  # Rotation angle in degrees

# Calculate radii
n_RadiusMax = n_DiameterMax / 2
n_RadiusMin = n_DiameterMin / 2

# Extract centromere coordinates (all rows except the last one)
centromeres = data.iloc[:-1].copy()

# Function to calculate distance from a point to the center of the ellipse
def distance_to_center(x, y, center_x, center_y):
    return np.sqrt((x - center_x)**2 + (y - center_y)**2)

# Function to calculate distance from center to ellipse edge through a point
def distance_to_edge(x, y, center_x, center_y, a, b, angle_deg):
    # Convert angle to radians
    angle_rad = np.deg2rad(angle_deg)
    
    # Translate point to origin
    x_t = x - center_x
    y_t = y - center_y
    
    # Rotate point to align ellipse with axes
    x_r = x_t * np.cos(-angle_rad) - y_t * np.sin(-angle_rad)
    y_r = x_t * np.sin(-angle_rad) + y_t * np.cos(-angle_rad)
    
    # Calculate angle to the point in the unrotated system
    theta = np.arctan2(y_r, x_r)
    
    # Calculate distance to ellipse edge along the line from center to point
    r = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)
    
    return r

# Calculate distances for each centromere
distances_to_center = []
distances_to_edge = []
distance_ratios = []
distances_to_periphery = []

for idx, centromere in centromeres.iterrows():
    x = centromere['X']
    y = centromere['Y']
    
    # Calculate distance from centromere to nucleus center
    d_center = distance_to_center(x, y, n_X, n_Y)
    distances_to_center.append(d_center)
    
    # Calculate distance from nucleus center to periphery through centromere
    d_edge = distance_to_edge(x, y, n_X, n_Y, n_RadiusMax, n_RadiusMin, n_RotAngle)
    distances_to_edge.append(d_edge)
    
    # Calculate ratio (percentage of distance from center to periphery)
    ratio = d_center / d_edge
    distance_ratios.append(ratio)
    
    # Calculate actual distance from centromere to periphery
    d_periphery = d_edge - d_center if d_center <= d_edge else 0
    distances_to_periphery.append(d_periphery)

# Add results to the dataframe
centromeres['Distance_to_Center'] = distances_to_center
centromeres['Center_to_Edge'] = distances_to_edge
centromeres['Distance_Ratio'] = distance_ratios
centromeres['Distance_to_Periphery'] = distances_to_periphery

# Display first few results
centromeres.head()

# Plot the results
plt.figure(figsize=(10, 8))

# Create ellipse
ellipse = Ellipse((n_X, n_Y), n_DiameterMax, n_DiameterMin, 
                  angle=n_RotAngle, 
                  fill=False, edgecolor='blue', linewidth=2)
ax = plt.gca()
ax.add_patch(ellipse)

# Plot centromeres
plt.scatter(centromeres['X'], centromeres['Y'], color='red', s=30)
plt.scatter([n_X], [n_Y], color='green', s=50, marker='x')  # Center of nucleus

# Set equal aspect ratio
plt.axis('equal')
plt.grid(True)
plt.title('Nucleus with Centromeres')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')

plt.show()

# Statistical summary of distances
print("Distance Statistics:")
print(centromeres[['Distance_to_Center', 'Center_to_Edge', 
                  'Distance_Ratio', 'Distance_to_Periphery']].describe())

# Create histograms
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.hist(centromeres['Distance_to_Center'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distance to Center')
plt.xlabel('Distance')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(centromeres['Center_to_Edge'], bins=15, color='lightgreen', edgecolor='black')
plt.title('Center to Edge Distance')
plt.xlabel('Distance')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
plt.hist(centromeres['Distance_Ratio'], bins=15, color='salmon', edgecolor='black')
plt.title('Distance Ratio (Center/Edge)')
plt.xlabel('Ratio')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)
plt.hist(centromeres['Distance_to_Periphery'], bins=15, color='purple', edgecolor='black', alpha=0.7)
plt.title('Distance to Periphery')
plt.xlabel('Distance')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Save results to CSV
result_df = pd.concat([centromeres, data.iloc[[-1]]], ignore_index=False)
result_df.to_csv('claude_centromere_distance_analysis.csv', index=False)