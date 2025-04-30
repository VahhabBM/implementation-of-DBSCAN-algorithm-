import numpy as np
import matplotlib.pyplot as plt
# data:
np.random.seed(42)
n = 500
x_o = np.array([.3, -1, -1.5])
y_o = np.array([-.6, -1.5, 2])
x_b = np.random.normal(-.25, .1, n // 5)
y_b = np.random.normal(0, .1, n // 5)
theta = np.random.uniform(0, 10, n)
r = .5 + .15 * theta
x_s = r * np.cos(theta)
y_s = r * np.sin(theta) + np.random.normal(0, .1, n)
x_1 = np.hstack([x_o, x_b, x_s])
x_2 = np.hstack([y_o, y_b, y_s])
X = np.vstack([x_1, x_2]).T

plt.figure(figsize=(8, 8))
plt.scatter(X[:, 0], X[:, 1])
plt.grid(True)
plt.show()
# dbscan implementation:

# we need to define a point class:
class Point:
    def __init__(self, x, y):
        self.cluster = None
        self.visited = False
        self.c_or_b = 'noise' #the points are noise by default!  
        self.x = x
        self.y = y

points = [Point(i[0], i[1]) for i in X]
# now this def, identifies which point is core and which one is border (we knew that the points are noise by default)
def dbscan(points, eps=0.2, minpts=4):
    for i in points:
        if i.visited:
            continue
        i.visited = True
        neighbors = []
        for j in points:
            dis = np.sqrt((i.x - j.x) ** 2 + (i.y - j.y) ** 2)
            if dis <= eps:
                neighbors.append(j)

        if len(neighbors) >= minpts:
            i.c_or_b = 'core'
            for neighbor in neighbors:
                if neighbor.c_or_b != 'core': 
                    neighbor.c_or_b = 'border'

dbscan(points)
# and this def identifies the clusters by the core/border/noise labels!
def identify_cluster(point, cluster, eps=0.2):
    if point.c_or_b == 'noise' or point.cluster is not None:
        return
    point.cluster = cluster
    neighbors = []
    for j in points:
        dis = np.sqrt((point.x - j.x) ** 2 + (point.y - j.y) ** 2)
        if dis <= eps:
            neighbors.append(j)

    for neighbor in neighbors:
        if neighbor.cluster is None:
            identify_cluster(neighbor, cluster)

cluster = 0
for i in points:
    if i.cluster is None and i.c_or_b == 'core':
        cluster += 1
        identify_cluster(i, cluster)

clusters = {}
for p in points:
    if p.cluster not in clusters:
        clusters[p.cluster] = []
    clusters[p.cluster].append((p.x, p.y))
# at the end we plot the result!!:
plt.figure(figsize=(8, 8))
colors = ['g', 'b', 'r', 'c', 'm', 'y', 'k']
for cluster_id, cluster_points in clusters.items():
    if cluster_id is None:
        label = 'Noise'
        color = 'gray'
    else:
        label = f'Cluster {cluster_id}'
        color = colors[(cluster_id - 1) % len(colors)]
    cluster_points = np.array(cluster_points)
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=color, label=label)

plt.legend()
plt.grid(True)
plt.show()
