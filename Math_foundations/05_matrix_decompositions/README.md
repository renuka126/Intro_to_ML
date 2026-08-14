
# Matrix Decompositions

I wanted to actually understand what `sklearn.decomposition.PCA()` does under the hood instead of just calling it — that meant learning eigendecomposition and SVD.

## Core ideas

**Eigenvalues and eigenvectors** — for a matrix A, an eigenvector v is a direction that doesn't get rotated when A is applied to it — it only gets scaled by a factor (the eigenvalue). Intuition: these are the "natural axes" of a transformation.

**Eigendecomposition** — breaking a (square) matrix down into its eigenvectors and eigenvalues. Useful, but only works cleanly for square matrices.

**SVD (Singular Value Decomposition)** — a generalization of eigendecomposition that works for *any* matrix, square or not. Decomposes a matrix A into `A = U Σ Vᵀ`, where Σ contains the "singular values" — essentially how much variance/importance each direction carries.

**Connection to PCA** — Principal Component Analysis finds the directions of maximum variance in your data. It does this by computing the eigenvectors of the data's covariance matrix (or equivalently, via SVD on the centered data matrix). The top eigenvectors *are* the principal components.

## Why it matters for ML

- PCA (dimensionality reduction) is eigendecomposition/SVD in disguise
- Recommender systems use SVD-based matrix factorization (e.g. predicting missing ratings)
- Understanding this makes "explained variance ratio" in PCA output actually meaningful instead of a black box number

## What's in the notebook

- Eigendecomposition of a small matrix by hand and with `numpy.linalg.eig`
- SVD on a real dataset (iris) and reconstructing it from fewer components
- Comparing my from-scratch PCA implementation to `sklearn.decomposition.PCA`
