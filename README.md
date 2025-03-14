# Centromere Distance Analysis

## Overview

This project analyzes the distances between centromeres and the periphery of the cell nucleus. The nucleus is modeled as an ellipse, and distances are calculated using two different methods:

1. **Radial Distance**: The distance from the centromere to the nucleus edge along the line connecting the centromere to the nucleus center.
2. **Shortest Distance**: The perpendicular distance from the centromere to the closest point on the nucleus edge.

The project also includes visualizations and statistical summaries to aid in interpretation.

## Features

- **Graphical User Interface (GUI)**: Built using Tkinter, allowing users to upload CSV files, compute distances, and export results.
- **Data Processing**: Reads centromere coordinates and nucleus ellipse parameters from a CSV file.
- **Distance Calculation**: Computes radial and shortest distances for each centromere.
- **Visualization**: Uses Matplotlib to generate graphical representations of centromere positions and distances.
- ![image](https://github.com/user-attachments/assets/8393e3c4-ab23-48ea-a747-85533c9b9782)
- **Statistical Analysis**: Provides insights into the distribution of centromere distances.
- ![image](https://github.com/user-attachments/assets/9e300955-fda7-47aa-8663-429e6ab88c20)


## Technologies Used

- **Python**: For data analysis and visualization.
- **Pandas & NumPy**: For numerical calculations and data handling.
- **Matplotlib**: For plotting centromere positions and nucleus boundaries.
- **SciPy**: For optimization functions.
- **Tkinter**: For creating the GUI.

## Installation

1. Clone the repository:
   ```sh
   git clone <repo_url>
   cd centromere-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the GUI application:
   ```sh
   python centromeres_gui.py
   ```
![image](https://github.com/user-attachments/assets/196ffe08-b998-428e-94b3-e70a21791e0f)

![image](https://github.com/user-attachments/assets/f5426eef-e20e-4e43-9834-b73189997fad)


## Usage

- **Data Input**: Provide a CSV file (`result_r.csv`) containing centromere coordinates and ellipse parameters.
- **Using the GUI**: The Tkinter-based application allows users to upload CSV files, start calculations, and export results.
- **Running Analysis via Script**: The script reads the data, computes distances, and generates visualizations.
- **Interpreting Results**: Outputs include statistical summaries and plots showing centromere-nucleus distances.

## Future Improvements

- Enhance statistical analysis with additional metrics.
- Implement interactive visualizations.
- Optimize performance for large datasets.

##

