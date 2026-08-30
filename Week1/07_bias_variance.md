# Bias-Variance Tradeoff

## The two sources of error

- **Bias** — error from wrong/oversimplified assumptions in the model (the model is too simple to capture the true pattern → underfitting)
- **Variance** — error from the model being too sensitive to the specific training data used (small changes in training data cause big changes in the model → overfitting)

## The decomposition

Total expected error can be broken down as:

Total Error = Bias^2 + Variance + Irreducible Error

- Irreducible error is noise in the data itself — no model can remove this (connects to the Bayes error rate idea from classification)

## The tradeoff

- Simple models (e.g., linear regression on complex data) → high bias, low variance
- Complex models (e.g., deep decision trees) → low bias, high variance
- The goal is to find the sweet spot that minimizes *total* error, not just one component

## My own example

Fitting a straight line to clearly curved data → high bias (it can never capture the curve, no matter how much data you give it). Fitting a super wiggly curve that passes through every single training point → high variance (a different training sample would produce a wildly different curve).

## Questions to revisit

- How do techniques like regularization (L1/L2) actually shift this tradeoff?
- How does this connect to the train/validation/test split we use in practice?