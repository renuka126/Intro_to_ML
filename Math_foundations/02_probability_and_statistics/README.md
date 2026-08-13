# Probability & Statistics

ML models make predictions under uncertainty — this folder is about the math that quantifies that uncertainty.

## Core ideas

**Random variables** — a variable whose value is the outcome of a random process (e.g. whether an email is spam).

**Mean, variance, standard deviation** — describe the center and spread of data. This is why we normalize/standardize features before training: it puts everything on a comparable scale so no single feature dominates due to its raw magnitude.

**Bayes' theorem**
```
P(A|B) = P(B|A) * P(A) / P(B)
```
Lets you update a belief (probability) given new evidence. Directly powers the Naive Bayes classifier — e.g. computing the probability an email is spam given the words it contains.

**Common distributions**
- **Normal (Gaussian)** — the classic bell curve. Used in weight initialization, assumptions behind many statistical tests.
- **Bernoulli** — a single yes/no trial. Basis of binary classification outputs.
- **Binomial** — repeated Bernoulli trials. Comes up in evaluating classifier accuracy over multiple trials.

**Expectation** — the long-run average value of a random variable. Loss functions in ML are often the *expected* loss over the data distribution.

## Why it matters for ML

- Naive Bayes classifiers are Bayes' theorem applied directly
- Data normalization relies on mean/variance
- Model outputs (e.g. softmax probabilities) are literally probability distributions
- Evaluation metrics like precision/recall are statistical in nature

## What's in the notebook

- Plotting normal, Bernoulli, and binomial distributions
- Simulating Bayes' theorem with a simple spam-filter-style example
- Computing mean/variance/std on a sample dataset and comparing before/after normalization
