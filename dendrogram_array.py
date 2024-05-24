#FALL21 Q.17
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import squareform, pdist
from sklearn.preprocessing import label_binarize
from apyori import apriori
from sklearn.cluster import KMeans
import sklearn.metrics as metrics
import pandas as pd


class cluster:
    def fancy_dendrogram(self, *args, **kwargs):
        max_d = kwargs.pop("max_d", None)
        if max_d and "color_threshold" not in kwargs:
            kwargs["color_threshold"] = max_d
        annotate_above = kwargs.pop("annotate_above", 0)

        ddata = dendrogram(*args, **kwargs)

        if not kwargs.get("no_plot", False):
            plt.title("Hierarchical Clustering Dendrogram (truncated)")
            plt.xlabel("sample index or (cluster size)")
            plt.ylabel("distance")
            for i, d, c in zip(ddata["icoord"], ddata["dcoord"], ddata["color_list"]):
                x = 0.5 * sum(i[1:3])
                y = d[1]
                if y > annotate_above:
                    plt.plot(x, y, "o", c=c)
                    plt.annotate(
                        "%.3g" % y,
                        (x, y),
                        xytext=(0, -5),
                        textcoords="offset points",
                        va="top",
                        ha="center",
                    )
            if max_d:
                plt.axhline(y=max_d, c="k")
        return ddata

    def dendro_plot(
        self,
        dist_df,
        Method,
        labels=None,
        sort=False,
        cutoff=None,
        show=True,
        invert_xaxis=True,
    ):

        if labels == None:
            labels = ["O{}".format(i) for i in range(1, dist_df.shape[1] + 1)]

        Z = squareform(dist_df)
        Z = linkage(Z, method=Method)
        # R = dendrogram(y, orientation = orientation, labels = labels, distance_sort = sort,truncate_mode='level', p=3)

        R = cluster.fancy_dendrogram(
            Z,
            leaf_rotation=90.0,
            leaf_font_size=12.0,
            show_contracted=True,
            annotate_above=10,
            max_d=cutoff,
            labels=labels,
        )
        plt.grid()
        if invert_xaxis:
            plt.gca().invert_xaxis()

        if show:
            plt.show()

        if cutoff != None:
            clusters = fcluster(Z, cutoff, criterion="distance")
            clusters = [c - 1 for c in clusters]
            return R, clusters
        else:
            return R
        
        
        

cluster = cluster()


data = """
0.0 3.7 3.4 2.3 1.8 1.6 2.4 2.6 2.5 4.3
3.7 0.0 3.2 5.1 3.5 2.9 4.4 4.6 4.0 7.2
3.4 3.2 0.0 4.1 2.6 4.0 2.7 5.3 2.9 6.1
2.3 5.1 4.1 0.0 3.7 3.2 1.7 2.7 1.9 2.6
1.8 3.5 2.6 3.7 0.0 2.8 3.2 4.4 3.4 5.6
1.6 2.9 4.0 3.2 2.8 0.0 3.4 2.1 3.1 5.3
2.4 4.4 2.7 1.7 3.2 3.4 0.0 3.8 0.8 4.1
2.6 4.6 5.3 2.7 4.4 2.1 3.8 0.0 3.5 4.0
2.5 4.0 2.9 1.9 3.4 3.1 0.8 3.5 0.0 4.4
4.3 7.2 6.1 2.6 5.6 5.3 4.1 4.0 4.4 0.0
"""




# Convert data to a 2D list
lines = data.strip().split('\n')
X = [list(map(float, line.split())) for line in lines]


#FALL 2017 Q.10


# Convert to a numpy array
X = np.array(X)


# Your data
#X = [[i] for i in [12, 17, 42, 48, 60]]

# Plot the dendrogram
cluster.dendro_plot(X, 'average')
#'single': uses the minimum of the distances between all observations of the two sets.
#'complete' or 'maximum': uses the maximum distances between all observations of the two sets.
#'average': uses the average of the distances of each observation of the two sets.
#centroid': uses the centroid of the distances of each observation of the two sets.
#'ward': uses the Ward variance minimization algorithm.


