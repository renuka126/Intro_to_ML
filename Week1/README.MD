# Week 1 — Introduction to Machine Learning

Notes and theory for Week 1 of the Introduction to Machine Learning course.
This week lays the conceptual foundation: what ML is, the three learning
paradigms, the formal decision-theoretic framework behind "good" predictions,
and why every model faces a bias-variance tradeoff.

---

## Topics Covered

1. **[Introduction to Machine Learning](01_intro_to_ml.md)** — what ML is,
   how it differs from traditional programming, and the three learning
   paradigms (supervised, unsupervised, reinforcement)
2. **[Supervised Learning](02_supervised_learning.md)** — learning a mapping
   from inputs to outputs using labeled data; regression vs classification
3. **[Unsupervised Learning](03_unsupervised_learning.md)** — finding
   structure (clusters, patterns, reduced representations) in unlabeled data
4. **[Reinforcement Learning](04_reinforcement_learning.md)** — an agent
   learning a policy through rewards and penalties from interacting with an
   environment
5. **[Statistical Decision Theory - Regression](05_statistical_decision_theory_regression.md)**
   — the formal framework for choosing the best predictor when the output is
   continuous (minimizing expected squared error)
6. **[Statistical Decision Theory - Classification](06_statistical_decision_theory_classification.md)**
   — the formal framework for choosing the best predictor when the output is
   a discrete label (minimizing expected misclassification / Bayes classifier)
7. **[Bias-Variance Tradeoff](07_bias_variance.md)** — why models underfit
   (high bias) or overfit (high variance), and how total error decomposes
   into bias² + variance + irreducible error

---

## Repo Structure

```
Week1/
├── README.md                                          <- this file
├── 01_intro_to_ml.md
├── 02_supervised_learning.md
├── 03_unsupervised_learning.md
├── 04_reinforcement_learning.md
├── 05_statistical_decision_theory_regression.md
├── 06_statistical_decision_theory_classification.md
└── 07_bias_variance.md
```

Each `.md` file covers one topic: core definitions, key formulas, and a short
example or intuition-building illustration where relevant.

---

## Concept Flow (why the topics are ordered this way)

```
Introduction to ML
      |
      v
Three Paradigms: Supervised / Unsupervised / Reinforcement
      |            (how a model can learn from data)
      v
Statistical Decision Theory — Regression
      |     (formalize "best predictor" for continuous y)
      v
Statistical Decision Theory — Classification
      |     (formalize "best predictor" for discrete y)
      v
Bias-Variance Tradeoff
      (why the "best predictor" in theory is hard to achieve in
       practice — every model trades off underfitting vs overfitting)
```

Week 1 moves from *what ML is* → *how a model can learn* → *what makes a
prediction "good," formally* → *why achieving "good" is fundamentally a
tradeoff*. Week 2 builds directly on this by applying the tradeoff to
concrete regression techniques (subset selection, shrinkage, PCR, PLS).

---

## Key Ideas Per Topic

| Topic | Core Question | Key Idea |
|---|---|---|
| Intro to ML | What is ML? | Learning patterns from data instead of hand-coded rules |
| Supervised Learning | Learn from labeled data | Map inputs → known outputs (regression/classification) |
| Unsupervised Learning | Learn from unlabeled data | Discover structure (clustering, dimensionality reduction) |
| Reinforcement Learning | Learn from feedback | Maximize cumulative reward via trial and error |
| Decision Theory (Regression) | Best predictor for continuous y | Minimize expected squared error → conditional mean $E[Y\|X=x]$ |
| Decision Theory (Classification) | Best predictor for discrete y | Minimize expected error → Bayes classifier (most probable class) |
| Bias-Variance Tradeoff | Why models under/overfit | Total error = Bias² + Variance + Irreducible Error |

---

## My Key Takeaway This Week

Everything this week builds toward one idea: ML is about picking a function
that predicts well on **new** data, not just data it's already seen.
Statistical decision theory gives the formal way to define "predicts well,"
and bias-variance explains why getting that right is a balancing act, not a
one-shot fix.

