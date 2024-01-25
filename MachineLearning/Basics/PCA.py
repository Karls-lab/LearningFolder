import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import make_classification

# Generate example data
X, y = make_classification(n_samples=100, n_features=10, n_classes=2, random_state=42)

# Apply PCA for dimensionality reduction
pca = PCA(n_components=2)  # Specify the number of components you want
X_pca = pca.fit_transform(X)

# Visualize the original and reduced data
plt.figure(figsize=(12, 5))

# Plot original data
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title("Original Data")

# Plot reduced data using the first two principal components
plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title("Data After PCA")

plt.show()

# Print the explained variance ratio
print("Explained Variance Ratio:")
print(pca.explained_variance_ratio_)
