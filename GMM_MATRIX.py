import numpy as np
#QUESTION 5 FALL 2018 
#GMM FROM DISTANCE MATRIX

# Define the observations and their mean vectors
o7 = np.array([1.92, 3.48, 2.11, 2.25, 2.38, 1.93, 0.0, 2.53, 2.09, 1.66])
o8 = np.array([1.58, 4.02, 1.15, 2.42, 1.53, 2.72, 2.53, 0.0, 1.68, 2.06])
o9 = np.array([1.08, 3.08, 1.09, 2.18, 1.71, 1.98, 2.09, 1.68, 0.0, 1.48])
o3 = np.array([0.63, 3.23, 0.0, 2.03, 1.06, 2.15, 2.11, 1.15, 1.09, 1.65])

# Define the parameters
sigma = 0.5
n_components = 3
# Define the size of the identity matrix (assuming a 8x8 identity matrix based on the problem)
identity_size = 10

# Calculate the density of each component at o3
component_densities = []
result = 0
i=0
distance_sq = [2.11, 1.15, 1.09] #03 to 07, 08, 09
for mean_vector in [o7, o8, o9]:
    component_density = (1 / (2 * np.pi * (sigma**2))**(identity_size/2)) * np.exp((-distance_sq[i]**2) / (2 * (sigma ** 2)))
    result +=(component_density/3)
    i+=1



# Print the rounded result
print("Density p(o3):", result)