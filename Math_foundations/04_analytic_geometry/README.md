# Analytic Geometry

Many ML algorithms are, at their core, asking "how far apart are these points?" or "which side of this line/plane does this point fall on?" This folder covers the geometry behind that.

## Core ideas

**Norms** — a way to measure the "length" of a vector.
- **L1 norm** — sum of absolute values. Basis of Lasso regression (encourages sparse weights, some become exactly zero).
- **L2 norm** — Euclidean length (square root of sum of squares). Basis of Ridge regression (shrinks weights smoothly, rarely to zero).

**Distance metrics**
- **Euclidean distance** — straight-line distance between two points. Used in KNN and K-means clustering.
- **Cosine similarity** — measures the angle between two vectors rather than their magnitude. Used heavily in text/embedding similarity, since it ignores document length.

**Projections** — mapping a point onto a line, plane, or subspace. Core to how PCA works (projecting high-dimensional data onto fewer dimensions while preserving as much variance as possible).

**Hyperplanes** — a flat decision boundary in n-dimensional space. This is exactly what a linear classifier (like a linear SVM or logistic regression) learns: the hyperplane that best separates classes.

## Why it matters for ML

- Regularization (Lasso/Ridge) is norm minimization
- KNN, K-means, and clustering algorithms are fundamentally distance calculations
- SVMs and linear classifiers directly learn hyperplanes
- PCA relies on projections

## What's in the notebook

- Computing Euclidean and cosine distance between sample points
- Visualizing a 2D hyperplane separating two classes
- Comparing L1 vs L2 norm penalty effects on a toy regression
