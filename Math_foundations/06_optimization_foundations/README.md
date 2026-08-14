# Optimization Foundations

Training a model is an optimization problem: find the weights that minimize the loss function. This folder is about the mechanics of how that search actually happens.

## Core ideas

**Convex vs non-convex functions** — a convex function has a single global minimum (think a bowl shape). A non-convex function can have many local minima and saddle points (think a mountain range). Most deep learning loss surfaces are non-convex, which is why training isn't guaranteed to find the *global* best solution — just a good enough one.

**Gradient descent** — the core training algorithm. At each step: compute the gradient of the loss with respect to the weights, then move the weights slightly in the opposite direction.
```
w_new = w_old - learning_rate * gradient
```

**Batch vs stochastic vs mini-batch gradient descent**
- **Batch** — uses the entire dataset to compute one gradient step. Accurate but slow, and doesn't fit in memory for large datasets.
- **Stochastic (SGD)** — uses a single example per step. Fast and noisy, but the noise can help escape shallow local minima.
- **Mini-batch** — a middle ground (e.g. 32 or 64 samples per step). What's actually used in practice.

**Learning rate** — controls step size. Too high → overshoots and diverges. Too low → training is painfully slow or gets stuck. Finding a good learning rate (or using an adaptive optimizer like Adam) is one of the most practical skills in ML.

## Why it matters for ML

- Every model I've trained relied on some flavor of gradient descent
- Understanding convexity explains why two training runs of the same model can converge differently
- Learning rate tuning is often the single biggest lever for getting a model to actually train well

## What's in the notebook

- From-scratch gradient descent on a toy loss function, plotting the convergence path
- Comparing batch, stochastic, and mini-batch gradient descent visually
- Demonstrating what happens with a learning rate that's too high vs too low
