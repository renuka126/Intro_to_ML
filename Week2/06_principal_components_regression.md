# Principal Components Regression (PCR)

## Motivation
When predictors are numerous and/or highly correlated, reduce dimensionality
**before** regressing, instead of selecting/shrinking individual predictors.

## How PCR Works
1. Perform **PCA (Principal Component Analysis)** on the predictor matrix X to get
   principal components $Z_1, Z_2, \dots, Z_M$ ($M \leq p$) — linear combinations
   of the original predictors that capture maximum variance in X, in decreasing order.
2. Regress the response $y$ on the first $M$ principal components (instead of the
   original p predictors) using ordinary least squares.
3. $M$ (number of components to keep) is chosen via **cross-validation**.

## Why It Helps
- Components are **uncorrelated (orthogonal)** by construction → eliminates
  multicollinearity entirely.
- Using fewer components ($M < p$) reduces variance, similar in spirit to
  shrinkage/subset selection.

## Key Limitation
PCA is **unsupervised** — it finds directions of maximum variance in X **without
looking at y**. There's no guarantee the top components are the ones most
predictive of the response. A component with high variance in X may be
irrelevant to y, while a low-variance component may matter a lot.

## PCR vs Ridge
Mathematically related — both shrink coefficients along the principal component
directions, but PCR discards low-variance directions completely (hard cutoff)
while Ridge shrinks continuously.

This limitation motivates **Partial Least Squares (PLS)**, which uses y when
constructing components.