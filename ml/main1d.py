import numpy as np
import matplotlib.pyplot as plt
# Generate sample data: heights of 250 people
heights = np.random.normal(170, 10, 250) # mean=170, std=10
# Create histogram
plt.hist(heights, bins=15, edgecolor='black')
plt.title("Histogram of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.savefig('height_histogram1.png')
