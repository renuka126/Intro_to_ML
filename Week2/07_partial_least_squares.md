# Partial Least Squares (PLS)

## Motivation
PCR's components are chosen without reference to the response y. **PLS** is a
supervised alternative — it finds new components that explain variance in X
**while also being correlated with y**.

## How PLS Works
1. Standardize all predictors.
2. Compute the first PLS component $Z_1$ as a weighted sum of predictors, where
   each predictor's weight is proportional to the coefficient from a **simple
   linear regression of y on that individual predictor** — so predictors more
   strongly related to y get higher weight.
3. To get $Z_2$: regress each predictor on $Z_1$, take the residuals (the part of
   each predictor not explained by $Z_1$), then repeat the weighting process on
   these residuals.
4. Continue until $M$ components are formed; regress y on $Z_1, \dots, Z_M$.
5. $M$ chosen via cross-validation, same as PCR.

## PLS vs PCR
| | PCR | PLS |
|---|---|---|
| Component construction | Unsupervised (uses only X) | Supervised (uses X and y) |
| Guarantees relevance to y | No | Directly optimizes for it |
| Bias/Variance | Can have lower bias if top PCs align with y | Often lower bias in practice, but can have higher variance if overfit to y |

## Practical Notes
- In practice, PLS doesn't always outperform PCR or Ridge — supervision helps
  reduce bias but can increase variance since components are fit to the
  (noisy) response.
- Popular in fields with many correlated predictors and limited samples, e.g.
  chemometrics, genomics.

## Week 2 Wrap-up
- **Linear/Multivariate Regression** → baseline models
- **Subset Selection** → pick a smaller predictor set (discrete choice)
- **Shrinkage (Ridge/Lasso)** → keep all predictors, shrink coefficients (continuous)
- **PCR/PLS** → reduce dimensionality via derived components instead of raw predictors