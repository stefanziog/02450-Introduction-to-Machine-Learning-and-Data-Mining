import numpy as np
import toolbox_extended as te


o7 = np.array([1.92, 3.48, 2.11, 2.25, 2.38, 1.93, 2.53, 2.09, 1.66])
o8 = np.array([1.58, 4.02, 1.15, 2.42, 1.53, 2.72, 2.53, 1.68, 2.06])
o9 = np.array([1.08, 3.08, 1.09, 2.18, 1.71, 1.98, 2.09, 1.68, 0.0, 1.48])
o4 = np.array([19.3, 35.5, 38.5])
print("density = ",te.density(o7) / np.mean([te.density(o8), te.density(o9)]))