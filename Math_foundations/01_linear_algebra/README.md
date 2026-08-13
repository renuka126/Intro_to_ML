# Linear Algebra

I started here because almost every ML model I use represents data as vectors and matrices under the hood. Before I could really trust what `model.fit(X, y)` was doing, I needed to understand what X and y actually *are* mathematically.

## Core ideas

**Vectors** — an ordered list of numbers. In ML, a single data point (a row of features) is a vector. A dataset is a stack of vectors, i.e. a matrix.

**Matrices** — a 2D array of numbers. Rows = samples, columns = features, in the most common ML convention.

**Dot product** — multiply corresponding elements of two vectors and sum them. This is the basis of:
- Cosine similarity (used in recommendation systems, embeddings)
- The weighted sum `w·x` inside every neuron of a neural network

**Matrix multiplication** — how a neural network layer transforms input into output: `y = Wx + b`. Every layer is just a matrix multiply plus a bias vector, followed by a non-linearity.

**Transpose** — flips rows and columns. Comes up constantly in backpropagation (gradients flow backward through transposed weight matrices).

**Identity and inverse** — the identity matrix is the "do nothing" transformation. The inverse of a matrix undoes what it does. In practice, ML rarely computes true inverses (too expensive/unstable) — this is why decompositions like SVD exist (see `05_matrix_decompositions`).

**Rank** — the number of linearly independent rows/columns in a matrix. Tells you how much "real" information the matrix carries. Low-rank matrices are the foundation of dimensionality reduction.

## Why it matters for ML

- Feature vectors are literally vectors in linear algebra's sense
- Neural network forward passes are matrix multiplications
- PCA, embeddings, and similarity search all rely on vector/matrix operations

## What's in the notebook

- Building a small feature matrix by hand
- Matrix multiplication done manually vs with `numpy`
- Transpose and rank computation
- Visualizing a 2D vector transformation (rotation and scaling) to build geometric intuition
