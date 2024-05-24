import numpy as np
import matplotlib.pyplot as plt

# Generate a grid of points
x1 = np.linspace(0, 6, 400)
x2 = np.linspace(0, 6, 400)
X1, X2 = np.meshgrid(x1, x2)

# Function to compute p-norm
def p_norm(x1, x2, p):
    return (np.abs(x1)**p + np.abs(x2)**p)**(1/p)

#FOR EUCLIDEAN CIRCLE
norm_2 = p_norm(X1, X2, 2)
#FOR INFINITY SQUARE
norm_inf = np.maximum(np.abs(X1), np.abs(X2))
# p-norm=1 
# TO CHANGE NORMS CHANGE THE NUMBER IN THE FUNCTION ,1,2,3 for p-norm=1,2,infinity
norm_A = p_norm(X1-2, X2, 1)

norm_B = p_norm(X1-2, X2-6, 1)
# p-norm=2
# p-norm=infinity
norm_C = p_norm(X1-6, X2-6, 2)

# Classification condition with additional X1 < 0.75 constraint
mask_A = (norm_A < 2) 
mask_B = (norm_B < 2)
mask_C = (norm_C < 3) 

#CLASSIFIER WIRH TREE
# mask_A = (X2>=0.54)
# mask_B = (X1>=0.5)
# mask_C = (X2>=0.35)
# mask_D = (X2>=0.26)

copy1 = (~mask_B&~mask_A) | (mask_B&~mask_C)
copy2 = mask_B&mask_C
copy3 = ~mask_B&mask_A

copyA = (mask_A )
copyB = (~mask_A) & (mask_B )
copyC = (~mask_A)& (~mask_B) &(mask_C)
copyNC = ~mask_A & ~mask_B & ~mask_C

# Setup plot
plt.figure(figsize=(8, 8))
plt.title('Classification Tree Visualization with X1 < 0.75 Constraint')
plt.xlabel('x1')
plt.ylabel('x2')

# Plot the regions according to the masks
plt.contourf(X1, X2, copyA, alpha=1, levels=[0.5, 1.5], colors=['red'], label='p-norm=1')
plt.contourf(X1, X2, copyB, alpha=1, levels=[0.5, 1.5], colors=['blue'], label='p-norm=2')
plt.contourf(X1, X2, copyC, alpha=1, levels=[0.5, 1.5], colors=['red'], label='p-norm=1')
plt.contourf(X1, X2, copyNC, alpha=1, levels=[0.5, 1.5], colors=['blue'], label='p-norm=1')

# plt.contourf(X1, X2, mask_inf, alpha=0.5, levels=[0.5, 1.5], colors=['red'], label='p-norm=Infinity')

# Add grid and lines for reference
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(True)

# Show the plot
plt.show()