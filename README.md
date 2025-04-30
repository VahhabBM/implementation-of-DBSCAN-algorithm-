# DBSCAN from Scratch (Density-Based Spatial Clustering)

This project implements the **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) algorithm from scratch in Python using only `numpy` and `matplotlib`.

DBSCAN is a powerful clustering algorithm that can identify clusters of arbitrary shape and also detect outliers (noise).

## 📌 What is DBSCAN?

DBSCAN groups together points that are close to each other based on a distance measurement and a minimum number of points. It categorizes each point as:

- **Core Point**: Has at least `minPts` neighbors within radius `eps`.
- **Border Point**: Has fewer than `minPts` neighbors but is in the neighborhood of a core point.
- **Noise**: Not a core or border point.

## 🔧 Parameters:

- `eps` (ε): The radius around a point to search for neighbors.
- `minpts`: The minimum number of points required to form a dense region (cluster).

## 🧪 Dataset:

- Synthetic 2D dataset with three types of data:
  - Outlier points (`x_o`, `y_o`)
  - Background noise (`x_b`, `y_b`)
  - Spiral pattern (`x_s`, `y_s`)

## 🧠 Implementation Steps:

### 1. **Data Generation**:
   - Random 2D dataset with clear clusters and noise for testing DBSCAN behavior.

### 2. **Point Class**:
Each point is represented as an instance of the `Point` class with attributes:
- `x, y`: coordinates
- `visited`: whether the point has been visited
- `cluster`: cluster ID
- `c_or_b`: core/border/noise label

### 3. **Core & Border Point Detection**:
The function `dbscan()` checks all points and marks them as core or border based on their neighborhood.

### 4. **Cluster Assignment**:
The function `identify_cluster()` uses DFS-like traversal to assign cluster IDs to core and border points.

### 5. **Visualization**:
Each cluster is plotted in a different color using `matplotlib`. Noise points are shown in gray.

## 📊 Results:

The algorithm successfully:
- Forms multiple clusters from arbitrary-shaped data.
- Identifies noise points correctly.
- Visualizes results with different colors for each cluster and gray for noise.

## 📌 Example Output Plot:

> 📷 A scatter plot showing clustered and noise points (generated using `matplotlib`).

## 📁 Dependencies:

- `numpy`
- `matplotlib`

## ✅ Conclusion:

This project shows how **DBSCAN** can be implemented from scratch without using any machine learning libraries. It demonstrates DBSCAN’s ability to:
- Handle noisy data
- Identify complex cluster shapes
- Automatically determine number of clusters (no need to specify `k`)

---
