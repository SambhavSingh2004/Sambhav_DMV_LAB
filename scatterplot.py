import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Dataset\Cleaned_Students_Performance.csv')

# Select meaningful columns
x = df['What was your previous SGPA?']
y = df['What is your current CGPA?']

# Create clusters (split data)
x1, y1 = x[:20], y[:20]
x2, y2 = x[20:40], y[20:40]

# Add slight positive correlation
y1 = y1 + x1 * 0.2
y2 = y2 + x2 * 0.2

# Add outliers
x_out = np.array([4.5, 1.5])
y_out = np.array([5.0, 1.0])

# Combine data
x_all = np.concatenate([x1, x2, x_out])
y_all = np.concatenate([y1, y2, y_out])

# Plot scatter graph
plt.figure()
plt.scatter(x_all, y_all)
plt.title("Scatter Plot (SGPA vs CGPA)")
plt.xlabel("Previous SGPA")
plt.ylabel("Current CGPA")
plt.show()