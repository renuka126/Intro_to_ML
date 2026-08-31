# Subset Selection — Part 2 (Stepwise Methods)

## Forward Stepwise Selection
1. Start with the **null model** (no predictors).
2. At each step, add the **one predictor** that most improves the model
   (largest reduction in RSS / best fit).
3. Repeat until all predictors are included.
4. Choose the best model among the sequence using $C_p$, AIC, BIC, adjusted R²,
   or cross-validation.

- Fits only $1 + p(p+1)/2$ models — far cheaper than best subset.
- Greedy: once a predictor is added, it's never removed, so it may miss the
  true best combination.

## Backward Stepwise Selection
1. Start with the **full model** (all predictors).
2. At each step, remove the **least useful predictor** (smallest impact on fit).
3. Repeat until only the intercept remains.
4. Choose the best model in the sequence, same criteria as forward selection.

- Also greedy, also cheap.
- Requires $n > p$ (needs more observations than predictors to fit the full model).

## Forward vs Backward vs Best Subset
| Method | Cost | Guarantees best model? | Requires n > p? |
|---|---|---|---|
| Best Subset | $2^p$ | Yes (exhaustive) | No |
| Forward Stepwise | $O(p^2)$ | No (greedy) | No |
| Backward Stepwise | $O(p^2)$ | No (greedy) | Yes |

## Model Selection via Cross-Validation
- Split data into k folds, fit candidate models on k−1 folds, validate on the
  held-out fold, average the error.
- Directly estimates test error — often preferred over AIC/BIC/$C_p$ in practice
  since it doesn't rely on distributional assumptions.