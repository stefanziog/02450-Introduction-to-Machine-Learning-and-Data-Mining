import numpy as np
from collections import Counter
import pandas as pd
# Convert labels into clusters that can be more easily compared
def cluster_similarity(x, y):
        """
        Parameters
        ----------
        x : Cluster A (labels)

        y : Cluster B

        Returns: Similarity Index - Rand und Jaccard
        eller den returnere ikke noget, den printer bare
        -------
        Copyright Peter Pik,
        Danmarks Tekniske Universitet
        """
        x = np.array(x)
        np.array(y)
        f00 = 0
        f01 = 0
        f10 = 0
        f11 = 0
        N = len(y)
        for i in range(N):
            for j in range(i):
                if y[i] != y[j] and x[i] != x[j]:
                    f00 += 1
                    # different class, different cluster
                elif y[i] == y[j] and x[i] == x[j]:
                    f11 += 1
                    # same class, same cluster
                elif y[i] == y[j] and x[i] != x[j]:
                    f10 += 1
                    # same class, different cluster
                else:
                    f01 += 1
                    # different class, same cluster

        rand = float(f00 + f11) / (f00 + f01 + f10 + f11)
        print("f00", f00)
        print("f11", f11)
        jaccard = float(f11) / (f01 + f10 + f11)

        similarities = [rand, jaccard]
        names = ["Rand", "Jaccard"]
        # for i in range(2):
        #     print(names[i],": ", similarities[i])

        result = pd.DataFrame({"Measure": names, "Value": similarities})
        print(result)
        return result


# Example data
Z = np.array([2, 3, 2, 2, 3, 3, 4, 2, 1, 1])
Q = np.array([1, 1, 1, 1, 2, 1, 2, 1, 3, 1])
cluster_similarity(Z, Q)

# Convert array labels to list of clusters


