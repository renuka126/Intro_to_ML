# Shrinkage Methods (Regularization)

## Motivation
Instead of selecting a subset of predictors, **fit all p predictors but constrain /
shrink** their coefficients toward zero. Reduces variance at the cost of a small
increase in bias — often improves prediction accuracy overall (bias-variance tradeoff).

## Ridge Regression
Adds an **L2 penalty** to the OLS objective:
$$
J(\beta) = \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p \beta_j^2
$$
- $\lambda \geq 0$ — tuning parameter controlling shrinkage strength
  ($\lambda = 0$ → OLS; $\lambda \to \infty$ → coefficients → 0)
- Shrinks correlated predictors' coefficients **toward each other**
- **Never sets coefficients exactly to zero** — keeps all predictors in the model
- Requires standardizing predictors first (penalty is scale-sensitive)

## Lasso Regression
Adds an **L1 penalty** instead:
$$
J(\beta) = \sum_{i=1}^n (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^p |\beta_j|
$$
- Can shrink coefficients **exactly to zero** → performs automatic **feature selection**
- Produces sparse, more interpretable models
- Preferred when only a subset of predictors truly matter

## Ridge vs Lasso
| | Ridge (L2) | Lasso (L1) |
|---|---|---|
| Coefficients | Shrunk, never zero | Can be exactly zero |
| Feature selection | No | Yes |
| Good when | Many small/medium effects | Few strong predictors, rest irrelevant |
| Handles multicollinearity | Very well | Reasonably |

## Choosing λ
- Selected via **cross-validation**: try a grid of λ values, pick the one minimizing
  CV error.

## Elastic Net (bonus)
Combines both penalties:
$$
\lambda \left[ \alpha \sum |\beta_j| + (1-\alpha) \sum \beta_j^2 \right]
$$
Balances sparsity (Lasso) with grouped shrinkage (Ridge).