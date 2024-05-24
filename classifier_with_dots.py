import numpy as np
import matplotlib.pyplot as plt
# Generate a grid of points
x1 = np.linspace(-1, 1, 400)
x2 = np.linspace(-1, 1, 400)
X1, X2 = np.meshgrid(x1, x2)

# Function to compute p-norm
def p_norm(x1, x2, p):
    return (np.abs(x1)**p + np.abs(x2)**p)**(1/p)

# Apply classification rules
# p-norm=1
norm_p1 = p_norm(X1, X2, 1)
#p-norm=2
norm_p2 = p_norm(X1, X2, 2)
# p-norm=infinity
norm_inf = np.maximum(np.abs(X1), np.abs(X2))

# Classification condition
mask_p1 = (norm_p1 < 0.5)
mask_both = (norm_p1 < 0.5) & (norm_inf < 0.375)
mask_rand = (norm_p2 > 1)

test_mask = (norm_inf)

#TRY IT OUT
norm_A = p_norm(X1-6, X2-4, 1)
norm_B = p_norm(X1-4, X2-2, 1)
norm_C = p_norm(X1-2, X2-4, 1)

mask_AB = (norm_A<3) & (norm_B<3)
mask_ANB = (norm_A<3) & (norm_B>3)
mask_AC = (norm_A<3) & (norm_C<3)
mask_ANC = (norm_A<3) & (norm_C>3)



# Create plot 
# TO CREATE MAKE THE CONDITION THAT THE MASK IS SATISFIED AND WHAT KIND OF DOT TO USE
plt.figure(figsize=(8, 8))
# Points where only norm_p1 condition is met
plt.scatter(X1[mask_AB], X2[mask_AB], c='blue', marker='o', label='Green dot (norm_p1 < 0.5)')
# Points where both conditions are met
plt.scatter(X1[mask_ANB], X2[mask_ANB], c='yellow', marker='o', label='Black dot (Both conditions)')
# Points where neither condition is met
plt.scatter(X1[mask_AC], X2[mask_AC], c='red', marker='+', label='Red plus (Outside norm_p1 < 0.5)')

plt.scatter(X1[mask_ANC], X2[mask_ANC], c='blue', marker='2', label='Red plus (Outside norm_p1 < 0.5)')


plt.title('Classification Tree Visualization')
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(True)
plt.legend()
plt.show()