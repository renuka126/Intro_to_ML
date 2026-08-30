# Unsupervised Learning

## Definition

Learning from data that has no labeled output — the model has to find structure, patterns, or groupings on its own.

## Common tasks

- **Clustering** — group similar points together (e.g., K-means)
- **Dimensionality reduction** — compress features while keeping important structure (e.g., PCA)
- **Density estimation** — model how data is distributed

## Why it's harder to evaluate

Unlike supervised learning, there's no "correct answer" to compare against, so evaluating whether an unsupervised model did a "good job" is more subjective (e.g., do the clusters actually make sense to a human?).

## My own example

Given customer purchase data with no predefined categories, clustering could reveal natural customer segments (budget shoppers, bulk buyers, brand-loyal buyers) without anyone telling the model these categories exist beforehand.

## Questions to revisit

- How do you choose the number of clusters (like `k` in K-means) without labeled ground truth?
- Where does dimensionality reduction fit before vs. after clustering?