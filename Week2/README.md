# Week 2 — Introduction to Machine Learning

Notes, theory, and worked implementations for Week 2 of the Introduction to
Machine Learning course. This week covers regression-based modeling: from a
single-predictor baseline all the way through dimensionality-reduction-based
regression techniques.

---

## Topics Covered

1. **Linear Regression** — single-predictor baseline model fit via Ordinary
   Least Squares (OLS)
2. **Multivariate Regression** — extending OLS to multiple predictors using
   matrix form and the normal equation
3. **Subset Selection — Part 1 (Best Subset)** — exhaustive search over all
   possible predictor combinations
4. **Subset Selection — Part 2 (Stepwise)** — cheaper greedy alternatives:
   forward and backward stepwise selection
5. **Shrinkage Methods** — Ridge (L2) and Lasso (L1) regression; regularizing
   coefficients instead of discarding predictors
6. **Principal Components Regression (PCR)** — regressing on PCA-derived
   components to remove multicollinearity
7. **Partial Least Squares (PLS)** — a supervised alternative to PCR that
   builds components using both X and y

Plus a graded assignment (Quiz: Week 2) and a non-graded practice assignment,
covering the same material.

---

## Repo Structure

```
Week2/
├── README.md                              <- this file
├── 01 linear regression.md                <- theory
├── 02_multivariate_regression.md          <- theory
├── 03_subset_selection_1.md               <- theory
├── 04_subset_selection_2.md               <- theory
├── 05_shrinkage_methods.md                <- theory
├── 06_principal_components_regression.md  <- theory
├── 07_partial_least_squares.md            <- theory
├── commands.ipynb                         <- all 7 topics, code + brief descriptions, single notebook
└── hours_vs_marks.py                      <- standalone Linear Regression script (toy dataset)
```

- **.md files** — theory notes: definitions, formulas, assumptions, and
  comparison tables for each topic. Read these first.
- **commands.ipynb** — one notebook containing all 7 topics in order, each
  with a short markdown description followed by tested, runnable code
  (sklearn / statsmodels). Executes top to bottom with no errors.
- **hours_vs_marks.py** — a minimal, standalone linear regression example
  (study hours to marks) if you just want the simplest possible working script
  without the full notebook.

---

## Concept Flow (why the topics are ordered this way)

```
Linear Regression
      |
      v
Multivariate Regression  --> adding more predictors introduces
      |                      multicollinearity & overfitting risk
      v
Subset Selection (Best Subset -> Stepwise)
      |   discrete choice: keep some predictors, drop the rest
      v
Shrinkage Methods (Ridge / Lasso)
      |   continuous choice: keep all predictors, shrink coefficients
      v
PCR --> reduce dimensionality via PCA components (unsupervised)
      |
      v
PLS --> same idea, but components are supervised (uses y too)
```

Each technique is a response to a limitation of the one before it — more
predictors improve fit but risk overfitting/multicollinearity, so later
sections trade a bit of bias for a lot less variance.

---

## Setup

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels
```

To run the combined notebook:

```bash
jupyter notebook commands.ipynb
```

or open it directly in VS Code with the Jupyter extension.

---

## Quick Reference — Metrics Used

| Metric | Used For | Meaning |
|---|---|---|
| MSE / RMSE / MAE | All regression models | Prediction error magnitude |
| R2 / Adjusted R2 | Model fit comparison | Variance explained (adjusted penalizes extra predictors) |
| VIF | Multivariate Regression | Detects multicollinearity |
| Cp / AIC / BIC / CV error | Subset Selection | Model size selection criteria |
| lambda | Ridge / Lasso | Regularization strength, tuned via CV |
| Explained variance ratio | PCR | How much predictor variance each component captures |

---
