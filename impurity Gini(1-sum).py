import numpy as np
#FALL 2017 Q.6

# Define the data
data = np.array([
    [0,1,4],  # f2 =1  
    [2,4,0],  # f2 =0  

])

# data = np.array([
#     [108, 112, 56],  # short players
#     [58, 75, 116],  # medium height players

# ])
#Different parent!

# Calculate the total number of samples for the parent node
total_samples_parent = 18 + 18 + 18
print(f"Total number of samples in the parent node: {total_samples_parent}")

# Calculate the impurity of the parent node
parent_proportions = np.array([18, 18, 18]) / total_samples_parent
parent_impurity = 1 - np.sum(parent_proportions**2)
print(f"Proportions of each class in the parent node: {parent_proportions}")
print(f"Impurity of the parent node: {parent_impurity}")

# Calculate the impurities of the child nodes
total_samples_children = np.sum(data, axis=1)  # total samples for each child node
child_proportions = data / total_samples_children[:, None]  # proportions for each child node
child_impurities = 1 - np.sum(child_proportions**2, axis=1)  # impurities for each child node
print(f"Proportions of each class in the child nodes: {child_proportions}")
print(f"Impurities of the child nodes: {child_impurities}")

# Calculate the weights for the child nodes
child_weights = total_samples_children / total_samples_parent
print(f"Weights of the child nodes: {child_weights}")

# Calculate the weighted sum of the impurities of the child nodes
weighted_child_impurities = np.sum(child_weights * child_impurities)
print(f"Weighted sum of the impurities of the child nodes: {weighted_child_impurities}")

# Calculate the impurity gain
impurity_gain = parent_impurity - weighted_child_impurities
print(f"Impurity Gain: {impurity_gain}")
