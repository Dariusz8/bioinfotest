#Trying and looking into various things while learning about bioinformatics
#Dariusz Czeczuk
#Start date: 10-25-2024
#Last mod: 11-02-2024

import numpy as np

# Define the array
genetic_markers = np.array([[0, 1, 1], [1, 0, 1], [0, 1, 1]])

# Calculate the distance matrix
distance_matrix = np.sqrt(((genetic_markers[:, np.newaxis] - genetic_markers) ** 2).sum(axis=2))

print(distance_matrix)
