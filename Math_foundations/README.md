# ML Math Foundations

This repo is where I'm building the math intuition behind the ML models I use. 
I got tired of calling `sklearn.fit()` without actually understanding what's 
happening underneath, so I started working through the core math topics — 
one folder per concept, with notes in my own words and a notebook that 
implements things from scratch before comparing to what a library gives you.

## Why this exists

I'm a Computer Engineering student specializing in ML Engineering, and I 
wanted a place to connect the math I'm learning (linear algebra, calculus, 
probability) directly to the ML concepts they power (gradient descent, PCA, 
regularization, Naive Bayes). This isn't a textbook dump — it's my own 
working-through of *why* each topic matters for ML, not just what it is.

## Structure

Each folder has:
- `README.md` — the concept explained in plain terms, with why it matters for ML
- `notebook.ipynb` — a from-scratch implementation, then a comparison to the 
  standard library version (numpy/scipy/sklearn)

## Topics

| # | Topic | What it connects to |
|---|-------|---------------------|
| 01 | [Linear Algebra](./01_linear_algebra) | Feature vectors, matrix ops, neural net layers |
| 02 | [Probability & Statistics](./02_probability_and_statistics) | Naive Bayes, data normalization, distributions |
| 03 | [Calculus](./03_calculus) | Gradients, backpropagation, loss functions |
| 04 | [Analytic Geometry](./04_analytic_geometry) | KNN, SVMs, distance-based models |
| 05 | [Matrix Decompositions](./05_matrix_decompositions) | PCA, dimensionality reduction |
| 06 | [Optimization Foundations](./06_optimization_foundations) | Gradient descent, convergence, learning rate |

## Notes

Work in progress — updating as I go through each topic in more depth. 
Feedback welcome.