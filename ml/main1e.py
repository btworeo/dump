import numpy as np
import matplotlib.pyplot as plt
# Number of preferences for different libraries
library = ['Matplotlib', 'Seaborn', 'Plotly', 'Plotnine']
chosen_by = [2500, 1800, 3000, 2200]
# Vertical Bar Plot
plt.bar(library, chosen_by, color='skyblue')
plt.xlabel('Visualization Library')
plt.ylabel('Number of Enthusiasts')
plt.title('Which Visualization Library Do People Prefer?')
plt.savefig('library_preferences1.png')
