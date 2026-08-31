# Subset Selection — Part 1

## Motivation
With many predictors, not all are useful. Subset selection chooses a **smaller set of
predictors** that gives good predictive performance while improving interpretability
and reducing variance.

## Best Subset Selection
1. For each $k = 0, 1, \dots, p$, fit **all** $\binom{p}{k}$ possible models
   containing exactly $k$ predictors.
2. Pick the best model of each size $k$ (lowest RSS / highest $R^2$).
3. Among the $p+1$ best models (one per size), select the final model using a
   metric that accounts for model complexity: **Cross-Validation, $C_p$, AIC, BIC,
   or Adjusted R²** (not plain RSS/R², which always favor more predictors).

## Selection Criteria
| Criterion | Idea |
|---|---|
| $C_p$ (Mallow's) | Adds a penalty for the number of predictors |
| AIC | Penalizes complexity; good for prediction-focused models |
| BIC | Stronger penalty than AIC; favors simpler models |
| Adjusted R² | Adjusts R² for number of predictors |
| Cross-Validation error | Directly estimates test-set performance |

## Drawback
Computationally expensive — $2^p$ models to fit. Infeasible for $p > \sim 40$.
This motivates **stepwise methods** (Part 2).